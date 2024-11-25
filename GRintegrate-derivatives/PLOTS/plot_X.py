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

## This is a code to genrate the analytic RDF
chi = 10
# Here chi is l
l = chi
x = np.linspace(0.01, 8, 500)

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

def h(x, l):
    return np.where(
        x < 0.95,
        0,
        1.5 * np.exp((1.0 - x) / l) * np.cos(2 * np.pi * (x - 1.05)) / x
    )

def qs(x, l):
    h_val = h(x, l)
    return (1 + h_val) * np.log(1 + h_val) - h_val

def u(x):
    return 2.1 / x**1.5


with plt.style.context([ 'ieee']):
    plt.rcParams['font.family'] = graphic_font
    plt.rcParams['mathtext.fontset'] = math_font
    plt.rcParams['text.usetex'] = True
    
    fig, ax = plt.subplots(figsize=plot_size)
    ax.spines['top'].set_linewidth(spine_width)    
    ax.spines['bottom'].set_linewidth(spine_width) 
    ax.spines['left'].set_linewidth(spine_width)   
    ax.spines['right'].set_linewidth(spine_width)
    
    
    Plot_KB     = plt.plot(x, h(x, l),
                    linestyle='solid',
                    linewidth= linewidth,
                    color='blue',
                    label=r"$q_{\rm KB}$")
    
    Plot_SEX    = plt.plot(x, qs(x, l),
                    linestyle='solid',
                    linewidth= linewidth,
                    color='red',
                    label=r"$q_{\rm S}$")
    
    Plot_KB_C   = plt.plot(x, u(x), linewidth=0.5, color="blue", linestyle='--', label=None)
    
    Plot_SEX_C  = plt.plot(x, u(x)**2, linewidth=0.5, color="red", linestyle='--', label=None)
    
    plot_Hline  = plt.axhline(0, color="black", linewidth=0.5, linestyle='-')
    
    plt.xlabel(r'$r$', fontsize=label_fontsize)
    plt.ylabel(r'$q(r)$',fontsize=label_fontsize)
    
    plt.xlim(0,8)
    plt.ylim(-1.1,1.6)
    
    ax.xaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_minor_locator(MultipleLocator(0.5))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))
    
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
    file_name = "FigureX.jpg"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')
    
    output_dir = os.getcwd()
    file_name = "FigureX.pdf"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight') 