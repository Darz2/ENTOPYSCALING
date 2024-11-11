#!/usr/bin/env python

########################### import the packages ############################

import os
import numpy as np
import scienceplots
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import ScalarFormatter, MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
from scipy.interpolate import interp1d

###################### MAIN_settings for plotting ###################

chi = 2
file_path   = rf"../integrateggr_{chi}.dat"
ggr          = np.loadtxt(file_path, skiprows=1)
ext_name    = rf"ext_ggr_{chi}.dat" 

########################### Plot settings ############################

plot_size = (4, 3)
graphic_font = 'Arial'
math_font = 'dejavuserif'  #['dejavusans', 'dejavuserif', 'cm', 'stix', 'stixsans', 'custom']
spine_width = 1
markersize=2
capsize=3
markeredgewidth=0.75
legend_linewidth = 1
linewidth =1                
tick_width=0.75
tick_length=4
minor_tick_width= 0.5
minor_tick_length=2
tick_labelsize=10
legend_fontsize=8
legend_boxwidth=0.75
label_fontsize=14
borderaxespad=0.6
resolution_value = 1200
break_threshold = 10
plt.rcParams['font.serif'] = graphic_font
plt.rcParams['mathtext.fontset'] = math_font

########################### FUNCTIONS ############################

# Extrapolating to x = 0
def extrapolate_to_zero(x,y):
    spline = interp1d(x, y, kind='linear', fill_value='extrapolate')
    x_ext = np.linspace(0, min(x), 100) 
    y_ext = spline(x_ext)
    
    return x_ext, y_ext

def plot_ggr(ggr):
    
    colors_indices_labels = [
        ('magenta', 4, '$X^{3}_{\infty}$'),
        ('g', 3, '$X^{2}_{\infty}$'),
        ('cyan', 5, '$X^{*} (L)$'),
        ('b', 1, '$X (L)$'),
        ('r', 2, '$X^{1}_{\infty}$')
    ]
    
    results = []
    
    x_ext, _ = extrapolate_to_zero(ggr[0:, 0], ggr[0:, 2])

    for color, index, label in colors_indices_labels:
        gr_line = plt.plot(ggr[0:, 0], ggr[0:, index], linestyle='solid', linewidth=linewidth, color=color, label=label)
        _, y_ext = extrapolate_to_zero(ggr[0:, 0], ggr[0:, index])  # Only y_ext changes per index
        gr_ext_line = plt.plot(x_ext, y_ext, color=color, linewidth=linewidth, linestyle=(0, (2, 2)))
        results.append((gr_line, gr_ext_line))

    return results



def plot_ggr_inset(ggr,filename=ext_name):
    
    x_ext, _ = extrapolate_to_zero(ggr[0:, 0], ggr[0:, 2])
    y_data = []
    
    with open(filename, 'w') as file:
        
        colors_indices_labels = [
            ('magenta', 4, '$X^{3}_{\infty}$'),#0
            ('g', 3, '$X^{2}_{\infty}$'), #1
            ('cyan', 5, '$X^{*} (L)$'), #2
            ('b', 1, '$X (L)$'), #3
            ('r', 2, '$X^{1}_{\infty}$') #4
        ]
        
        reorder_write = [3, 4, 1, 0, 2]
        results = []
        
        for color, index, label in colors_indices_labels:
            gr_line = plt.plot(ggr[0:, 0], ggr[0:, index], linestyle='solid', linewidth=linewidth, color=color)
            _, y_ext = extrapolate_to_zero(ggr[0:, 0], ggr[0:, index])  # Only y_ext changes
            gr_ext_line = plt.plot(x_ext, y_ext, color=color, linewidth=linewidth, linestyle=(0, (2, 2)))
            results.append((gr_line, gr_ext_line))
            y_data.append(y_ext)
            
        # Header
        file.write("x_ext\t" + "\t".join([rf"{colors_indices_labels[i][2]}" for i in reorder_write]) + "\n")

        # Write x_ext values and reordered y_ext columns
        for i in range(len(x_ext)):
            file.write(f"{x_ext[i]}")
            for j in reorder_write:
                file.write(f"\t{y_data[j][i]}")
            file.write("\n")
        
        dummy_line = plt.Line2D([], [], color='black', linewidth=linewidth, linestyle=(0, (2, 2)), label='$L \\to \\infty$')
        combined_legend = plt.legend([dummy_line], ['$L \\to \\infty$'],
                                     fontsize=legend_fontsize, loc=4, ncol=1,
                                     framealpha=1, borderaxespad=1)
        outline = combined_legend.get_frame()
        outline.set_linewidth(legend_boxwidth)
        outline.set_edgecolor('black')   

    return results


with plt.style.context([ 'ieee']):
    plt.rcParams['font.family'] = graphic_font
    plt.rcParams['mathtext.fontset'] = math_font
    plt.rcParams['text.usetex'] = True
    fig, ax = plt.subplots(figsize=plot_size)
    ax.spines['top'].set_linewidth(spine_width)    
    ax.spines['bottom'].set_linewidth(spine_width) 
    ax.spines['left'].set_linewidth(spine_width)   
    ax.spines['right'].set_linewidth(spine_width)  
    
    plot_ggr(ggr)
    
    plt.xlabel(r'$1/L$',fontsize=label_fontsize)
    plt.ylabel(r'$X$',fontsize=label_fontsize)
    
    # plt.xlim(0, 0.5)
    plt.xlim(-0.01, 0.5)
    plt.ylim(1.5,15)
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.05))
    ax.yaxis.set_major_locator(MultipleLocator(2))
    ax.yaxis.set_minor_locator(MultipleLocator(1))
    
    ax.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
                bottom=True, top=True, left=True, right=True)
    ax.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)
    
    
    handles, labels = plt.gca().get_legend_handles_labels()
    
    order = [3, 4, 1, 0, 2]  # order of lables
    
    # Combine all legend settings into one call
    combined_legend = plt.legend([handles[idx] for idx in order], 
                                 [labels[idx] for idx in order],
                                 fontsize=legend_fontsize, 
                                 loc=3, 
                                 ncol=1, 
                                 framealpha=1,
                                 borderaxespad=1)
    
    #outline1 = combined_legend.get_frame().set_alpha(0)
    outline = combined_legend.get_frame()
    outline.set_linewidth(legend_boxwidth)
    outline.set_edgecolor('black')
    
    ax_inset = inset_axes(ax, width="50%", height="100%", loc='center left',
                      bbox_to_anchor=(1.15, 0.0, 1, 1), 
                      bbox_transform=ax.transAxes, borderpad=1)

    plot_ggr_inset(ggr)
    
    # ax_inset.text(0.15, 0.75, '$L$ = $\infty$', transform=ax_inset.transAxes, 
    #           fontsize=8, fontweight='bold',
    #           ha='center', va='center')
    
    ax_inset.set_xlabel(r'$1/L$',  fontsize=label_fontsize)
    # ax_inset.set_ylabel(r'$X$',labelpad=0,fontsize=label_fontsize)
    
    ax_inset.set_xlim(0.00, 0.13)  
    ax_inset.set_ylim(10.9, 11.7)   
    
    # ax_inset.set_xlim(-0.005, 0.05)  
    # ax_inset.set_ylim(10.9, 11.7) 
    
    ax_inset.xaxis.set_major_locator(MultipleLocator(0.05))
    ax_inset.xaxis.set_minor_locator(MultipleLocator(0.025))
    ax_inset.yaxis.set_major_locator(MultipleLocator(0.2))
    ax_inset.yaxis.set_minor_locator(MultipleLocator(0.1))
    
    ax_inset.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
                bottom=True, top=True, left=True, right=True)
    ax_inset.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)

    for line in ax_inset.get_lines():
        line.set_zorder(1)
        
    output_dir = os.getcwd()
    file_name = rf"integrate_ggr_{chi}.jpg"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')
    
    output_dir = os.getcwd()
    file_name = rf"integrate_ggr_{chi}.pdf"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')