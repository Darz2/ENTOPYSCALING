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
import matplotlib.cm as cm

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

def wf_potential(r, rc, alpha, Lambda):
    f1 = r**2 + alpha * (1 - Lambda)
    f2 = (1 / f1) - 1
    f3 = rc**2 + alpha * (1 - Lambda)
    f4 = ((f3 / f1) - 1)**2
    return Lambda * f2 * f4

epsilon = 1.0
sigma = 1.0
rc = 2
alpha = np.arange(0,1.01,0.01)
Lambda = 0.5
highlight_alpha = [0.1, 0.5, 0.9]

# cmap = cm.get_cmap("viridis")
cmap = cm.get_cmap("coolwarm")
norm = mcolors.Normalize(vmin=min(alpha), vmax=max(alpha))  #

with plt.style.context([ 'ieee']):
    plt.rcParams['font.family'] = graphic_font
    plt.rcParams['mathtext.fontset'] = math_font
    plt.rcParams['text.usetex'] = True
    fig, ax = plt.subplots(figsize=plot_size)
    ax.spines['top'].set_linewidth(spine_width)    
    ax.spines['bottom'].set_linewidth(spine_width) 
    ax.spines['left'].set_linewidth(spine_width)   
    ax.spines['right'].set_linewidth(spine_width) 

    for i, alpha_val in enumerate(alpha):
        
        r = np.linspace(0, 2, 5000)
        V_WF = wf_potential(r, rc, alpha_val, Lambda)
        color = cmap(norm(alpha_val))
        
        # plt.plot(r, V_WF, label=rf"{i}", color= color, linestyle='solid', linewidth=linewidth)
        # plt.axhline(0, color='black',linewidth=0.5)
        # plt.axvline(2.0 * sigma, color='red', linestyle='--', label="Rcut")
        
        if any(np.isclose(alpha_val, ha, atol=1e-3) for ha in highlight_alpha):
            # midpoint_idx = len(r) // 2  # Index at the middle
            
            zero_crossings = np.where(np.abs(V_WF) < 1e-1)[0]
            # print(zero_crossings[0])
            
            midpoint_1 = zero_crossings[0] - 20
            # print(midpoint_1)
            midpoint_3 = zero_crossings[0] 
            midpoint_2 = zero_crossings[0] + 20
            
            # midpoint_1 = 3000
            # midpoint_3 = 3150
            # midpoint_2 = 3300
            
            ax.plot(r[:midpoint_1], V_WF[:midpoint_1], color='k', linestyle='solid', linewidth=1.2)
            ax.plot(r[midpoint_2:], V_WF[midpoint_2:], color='k', linestyle='solid', linewidth=1.2)
            
            # Add text at the break point
            ax.text(
                r[midpoint_3], V_WF[midpoint_3], f"{alpha_val:.1f}",
                fontsize=legend_fontsize-2,
                fontweight='bold',
                color='black',
                ha='center',  # Center the text horizontally
                va='center',  # Center the text vertically
                bbox=dict(facecolor='white', edgecolor='none', pad=0.5, alpha=0.0)
            )
        else:
            ax.plot(r, V_WF, color=color, linestyle='solid', linewidth=linewidth)
        
    plt.xlabel("$r$", fontsize=label_fontsize)
    plt.ylabel("$U_{\mathrm{WF}}(r)$", fontsize=label_fontsize)
    
    plt.xlim(0.45,2)
    plt.ylim(-1.1, 1.1)
    
    # Add a color bar
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=norm)
    sm.set_array([])  # Dummy array for ScalarMappable
    cbar = plt.colorbar(sm, ax=ax, orientation='vertical', pad=0.08)
    cbar.set_label(r"$\alpha$", labelpad=-40, fontsize=label_fontsize)  # Label for color bar
    cbar.ax.tick_params(labelsize=tick_labelsize) 
    
    ax.tick_params(axis='both', which='major', direction='in', width=tick_width, length=tick_length, labelsize=tick_labelsize,
            bottom=True, top=True, left=True, right=True)
    ax.tick_params(axis='both', which='minor', direction='in', width=minor_tick_width, length=minor_tick_length,
                bottom=True, top=True, left=True, right=True)
    
    ax.xaxis.set_major_locator(MultipleLocator(0.5))
    ax.xaxis.set_minor_locator(MultipleLocator(0.25))
    ax.yaxis.set_major_locator(MultipleLocator(0.5))
    ax.yaxis.set_minor_locator(MultipleLocator(0.25))
    
    # combined_legend = plt.legend(fontsize=legend_fontsize, loc=1, ncol=1,borderaxespad=1)
    # #outline1 = combined_legend.get_frame().set_alpha(0)
    # outline = combined_legend.get_frame()
    # outline.set_linewidth(legend_boxwidth)
    # outline.set_edgecolor('black')
    # # plt.grid(True)
    
    output_dir = os.getcwd()
    file_name = f"WF_alpha.jpg"
    file_path = os.path.join(output_dir, file_name)
    fig.savefig(file_path, dpi=resolution_value, bbox_inches='tight')
    fig.savefig(fr"{file_name}", dpi=resolution_value, bbox_inches='tight')
