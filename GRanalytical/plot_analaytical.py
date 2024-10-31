#!/usr/bin/env python

########################### import the packages ############################
import sys
import os
import math
import numpy as np
import scienceplots
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

file_path   = "gr_2.dat"
gr_2         = np.loadtxt(file_path, skiprows=1)

file_path   = "gr_5.dat"
gr_5       = np.loadtxt(file_path, skiprows=1)

file_path   = "gr_10.dat"
gr_10       = np.loadtxt(file_path, skiprows=1)

file_path   = "gr_15.dat"
gr_15       = np.loadtxt(file_path, skiprows=1)

file_path   = "gr_20.dat"
gr_20       = np.loadtxt(file_path, skiprows=1)


with plt.style.context([ 'ieee']):
    plt.rcParams['font.family'] = graphic_font
    plt.rcParams['mathtext.fontset'] = math_font
    plt.rcParams['text.usetex'] = True
    fig, ax = plt.subplots(figsize=plot_size)
    ax.spines['top'].set_linewidth(spine_width)    
    ax.spines['bottom'].set_linewidth(spine_width) 
    ax.spines['left'].set_linewidth(spine_width)   
    ax.spines['right'].set_linewidth(spine_width)  

    plot_1 = plt.plot(gr_2[0:,0], gr_2[0:,1],
                    linestyle= 'solid',
                    color='r',
                    label='$\chi = 2$')
    
    plot_1 = plt.plot(gr_5[0:,0], gr_5[0:,1],
                    linestyle= 'solid',
                    color='magenta',
                    label='$\chi = 5$')
        
    plot_1 = plt.plot(gr_10[0:,0], gr_10[0:,1],
                    linestyle= 'solid',
                    color='b',
                    label='$\chi = 10$')
            
    plot_1 = plt.plot(gr_15[0:,0], gr_15[0:,1],
                    linestyle= 'solid',
                    color='cyan',
                    label='$\chi = 15$')
                
    plot_5 = plt.plot(gr_20[0:,0], gr_20[0:,1],
                    linestyle= 'solid',
                    color='g',
                    label='$\chi = 20$')
        
    plt.xlabel(r'$r$', fontsize=label_fontsize)
    plt.ylabel(r'$g(r)$',fontsize=label_fontsize)
    
    plt.xlim(0, 4)
    # plt.ylim(0, 2)
    # ax.xaxis.set_major_locator(MultipleLocator(0.2))
    # ax.xaxis.set_minor_locator(MultipleLocator(10))
    
    ax.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
                bottom=True, top=True, left=True, right=True)
    ax.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)
    
    combined_legend = plt.legend(fontsize=legend_fontsize, loc=1, ncol=1,borderaxespad=1)
    #outline1 = combined_legend.get_frame().set_alpha(0)
    outline = combined_legend.get_frame()
    outline.set_linewidth(legend_boxwidth)
    outline.set_edgecolor('black')

    output_dir = os.getcwd()
    file_name = f"analytical_gr.jpg"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')
