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
from scipy.interpolate import interp1d

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

chi = 2

file_path   = rf"../integrategr_{chi}.dat"
gr         = np.loadtxt(file_path, skiprows=1)

# Extrapolating to x = 0
def extrapolate_to_zero(x,y):
    spline = interp1d(x, y, kind='linear', fill_value='extrapolate')
    x_ext = np.linspace(0, min(x), 100) 
    y_ext = spline(x_ext)
    
    return x_ext, y_ext

def plot_gr(gr):
     
    
    gr_3 = plt.plot(gr[0:,0], gr[0:,4],
                    linestyle= 'solid', linewidth=linewidth,
                    color='magenta',
                    label='$X^{3}_{\infty}$')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,3])
    gr_ext3        = plt.plot(x_ext, y_ext, color='k',  linewidth=linewidth, linestyle=(0, (2, 2)))
    
    
    
    gr_2 = plt.plot(gr[0:,0], gr[0:,3],
                    linestyle= 'solid', linewidth=linewidth,
                    color='g',
                    label='$X^{2}_{\infty}$')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,3])
    gr_ext2        = plt.plot(x_ext, y_ext, color='k', linewidth=linewidth,  linestyle=(0, (2, 2)))
    
    
    gr_4 = plt.plot(gr[0:,0], gr[0:,5],
                    linestyle= 'solid', linewidth=linewidth,
                    color='cyan',
                    label='$X^{*} (L) $')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,5])
    gr_ext4        = plt.plot(x_ext, y_ext, color='k', linewidth=linewidth , linestyle=(0, (2, 2)))
    
    
    gr_0 = plt.plot(gr[0:,0], gr[0:,1],
                    linestyle= 'solid', linewidth=linewidth,
                    color='b',
                    label='$X (L)$')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,1])   
    gr_ext0        = plt.plot(x_ext, y_ext, color='k', linewidth=linewidth, linestyle=(0, (2, 2)))
 
    
    
    gr_1 = plt.plot(gr[0:,0], gr[0:,2],
                    linestyle= 'solid', linewidth=linewidth,
                    color='r',
                    label='$X^{1}_{\infty}$')  
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,2]) 
    gr_ext1        = plt.plot(x_ext, y_ext, color='k',linewidth=linewidth,  linestyle=(0, (2, 2)))
    
    return gr_0, gr_ext0, gr_1, gr_ext1, gr_2, gr_ext2,  gr_3, gr_ext3,  gr_4, gr_ext4


def plot_gr_inset(gr):
            
    
    gr_3 = plt.plot(gr[0:,0], gr[0:,4],
                    linestyle= 'solid', linewidth=linewidth,
                    color='magenta')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,4])
    gr_ext3        = plt.plot(x_ext, y_ext, color='k', linewidth=linewidth, linestyle=(0, (2, 2)))
    
    
    
    gr_2 = plt.plot(gr[0:,0], gr[0:,3],
                    linestyle= 'solid', linewidth=linewidth,
                    color='g')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,3])
    gr_ext2        = plt.plot(x_ext, y_ext, color='k', linewidth=linewidth, linestyle=(0, (2, 2)))
    
    
    
    gr_4 = plt.plot(gr[0:,0], gr[0:,5],
                    linestyle= 'solid',     linewidth=linewidth,
                    color='cyan')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,5])
    gr_ext4        = plt.plot(x_ext, y_ext, color='k',linewidth=linewidth, linestyle=(0, (2, 2)))
    
    
    gr_0 = plt.plot(gr[0:,0], gr[0:,1],
                    linestyle= 'solid', linewidth=linewidth,
                    color='b')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,1])
    gr_ext0        = plt.plot(x_ext, y_ext, color='k', linewidth=linewidth, linestyle=(0, (2, 2)), label='$R \\to \\infty$')
    combined_legend = plt.legend(fontsize=legend_fontsize, 
                                 loc=3, 
                                 ncol=1,
                                 framealpha=1, 
                                 borderaxespad=1)
    outline = combined_legend.get_frame()
    outline.set_linewidth(legend_boxwidth)
    outline.set_edgecolor('black')
    
    
    
    gr_1 = plt.plot(gr[0:,0], gr[0:,2],
                    linestyle= 'solid',     linewidth=linewidth,
                    color='r',
                    label='$X^{1}_{\infty}$')
    x_ext, y_ext    = extrapolate_to_zero(gr[0:,0], gr[0:,2])
    gr_ext1        = plt.plot(x_ext, y_ext, color='k',linewidth=linewidth,  linestyle=(0, (2, 2)))
    
    
    
    return gr_0, gr_ext0, gr_1, gr_ext1, gr_2, gr_ext2,  gr_3, gr_ext3,  gr_4, gr_ext4


with plt.style.context([ 'ieee']):
    plt.rcParams['font.family'] = graphic_font
    plt.rcParams['mathtext.fontset'] = math_font
    plt.rcParams['text.usetex'] = True
    fig, ax = plt.subplots(figsize=plot_size)
    ax.spines['top'].set_linewidth(spine_width)    
    ax.spines['bottom'].set_linewidth(spine_width) 
    ax.spines['left'].set_linewidth(spine_width)   
    ax.spines['right'].set_linewidth(spine_width)  
    
    plot_gr(gr)
    
    plt.xlabel(r'$1/R$', fontsize=label_fontsize)
    plt.ylabel(r'$G_{\infty}$',fontsize=label_fontsize)
    
    # plt.xlim(0, 0.5)
    plt.xlim(-0.01, 0.32)
    # plt.ylim(-35, 35)
    ax.xaxis.set_major_locator(MultipleLocator(0.1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.05))
    
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
                                 loc=2, 
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

    plot_gr_inset(gr)
    
    ax_inset.set_xlabel(r'$1/R$',  fontsize=label_fontsize)
    ax_inset.set_ylabel(r'$G_{\infty}$',labelpad=-7, fontsize=label_fontsize)
    
    ax_inset.set_xlim(0, 0.09)  # X-axis limit for zoom
    ax_inset.set_ylim(-2.15, -1.95)   # Y-axis limit for zoom
    
    ax_inset.xaxis.set_major_locator(MultipleLocator(0.04))
    ax_inset.xaxis.set_minor_locator(MultipleLocator(0.02))
    ax_inset.yaxis.set_major_locator(MultipleLocator(0.1))
    ax_inset.yaxis.set_minor_locator(MultipleLocator(0.05))
    
    ax_inset.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
                bottom=True, top=True, left=True, right=True)
    ax_inset.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)
    
    output_dir = os.getcwd()
    file_name = rf"integrate_gr_{chi}.jpg"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')