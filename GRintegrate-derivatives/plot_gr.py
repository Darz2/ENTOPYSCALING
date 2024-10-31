#!/usr/bin/env python

########################### import the packages ############################
import os
import numpy as np
import scienceplots
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.ticker import ScalarFormatter, MultipleLocator
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

markers = ['o', 's', '^', 'D', 'h', '*', 'X' , "8"]
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
alpha = 1
CO2_color = '#e41a1c'
MIX_color = '#008000'
rgba_CO2_color = mcolors.to_rgba(CO2_color)
rgba_MIX_color = mcolors.to_rgba(MIX_color)
CO2_face_color = (rgba_CO2_color[0], rgba_CO2_color[1], rgba_CO2_color[2], 0.6)
MIX_face_color = (rgba_MIX_color[0], rgba_MIX_color[1], rgba_MIX_color[2], 0.6)
resolution_value = 1200
break_threshold = 10 # for NIST data
plt.rcParams['font.serif'] = graphic_font
plt.rcParams['mathtext.fontset'] = math_font

file_path   = "integrategr_10.dat"
gr         = np.loadtxt(file_path, skiprows=1)

def plot_ggr(gr):
    
    gr_0 = plt.plot(gr[0:,0], gr[0:,1],
                    linestyle= 'solid',
                    color='b',
                    label='$X (L)$')
    
    gr_1 = plt.plot(gr[0:,0], gr[0:,2],
                    linestyle= 'solid',
                    color='r',
                    label='$X^{1}_{\infty}$')
    
    gr_2 = plt.plot(gr[0:,0], gr[0:,3],
                    linestyle= 'solid',
                    color='g',
                    label='$X^{2}_{\infty}$')
    
    # gr_3 = plt.plot(gr[0:,0], gr[0:,4],
    #                 linestyle= 'solid',
    #                 color='magenta',
    #                 label='$X^{3}_{\infty}$')
    
    # gr_4 = plt.plot(gr[0:,0], gr[0:,5],
    #                 linestyle= 'solid',
    #                 color='cyan',
    #                 label='$X^{*} (L) $')
    
    return gr_0, gr_1

with plt.style.context([ 'ieee']):
    plt.rcParams['font.family'] = graphic_font
    plt.rcParams['mathtext.fontset'] = math_font
    plt.rcParams['text.usetex'] = True
    fig, ax = plt.subplots(figsize=plot_size)
    ax.spines['top'].set_linewidth(spine_width)    
    ax.spines['bottom'].set_linewidth(spine_width) 
    ax.spines['left'].set_linewidth(spine_width)   
    ax.spines['right'].set_linewidth(spine_width)  
    
    plot_ggr(gr)
    
    plt.xlabel(r'$1/R$', fontsize=label_fontsize)
    plt.ylabel(r'$G_{\infty}$',fontsize=label_fontsize)
    
    # plt.xlim(0, 0.5)
    plt.xlim(0, 0.2)
    # ax.xaxis.set_major_locator(MultipleLocator(0.2))
    # ax.xaxis.set_minor_locator(MultipleLocator(10))
    
    ax.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
                bottom=True, top=True, left=True, right=True)
    ax.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)
    
    combined_legend = plt.legend(fontsize=legend_fontsize, loc=4, ncol=1,borderaxespad=1)
    #outline1 = combined_legend.get_frame().set_alpha(0)
    outline = combined_legend.get_frame()
    outline.set_linewidth(legend_boxwidth)
    outline.set_edgecolor('black')
    
    ax_inset = inset_axes(ax, width="50%", height="100%", loc='center left',
                      bbox_to_anchor=(1.15, 0.0, 1, 1), 
                      bbox_transform=ax.transAxes, borderpad=1)

    plot_ggr(gr)
    
    ax_inset.set_xlim(0, 0.02)  # X-axis limit for zoom
    ax_inset.set_ylim(-2.5, -2)   # Y-axis limit for zoom
    
    ax_inset.xaxis.set_major_locator(MultipleLocator(0.01))
    ax_inset.xaxis.set_minor_locator(MultipleLocator(0.005))
    ax_inset.yaxis.set_major_locator(MultipleLocator(0.1))
    ax_inset.yaxis.set_minor_locator(MultipleLocator(0.05))
    
    ax_inset.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
                bottom=True, top=True, left=True, right=True)
    ax_inset.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)
    
    output_dir = os.getcwd()
    file_name = f"integrate_gr.jpg"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')