# -*- coding: utf-8 -*-
"""
:author: Tim Häberlein
:version: 1.0
:date: 15.03.2024
:organisation: TU Dresden, FZM
"""

# -------- start import block ---------
import matplotlib as mpl  # import matplotlib as mpl and set pgf as backend
import matplotlib.pyplot as plt  # eigentliche plot-Bibliothek
import matplotlib.ticker as ticker
import numpy as np  # numpy für arrays und so
import copy


# -------- end import block ---------


# class für tud farben

class RGBColor(object):
    """
    Klasse für die RGB-Farben.
    """

    def __init__(self, r: int, g: int, b: int):
        """
        Constructor for the RGBColor class. Initializes the color attributes.

       Args:
       - r (int): Red component of the color.
       - g (int): Green component of the color.
       - b (int): Blue component of the color.
       """
        self.r = r
        self.g = g
        self.b = b
        self.items = [self.r, self.g, self.b]
        self.index = 0

    def __iter__(self):
        #return tuple({self.r, self.g, self.b})
        return iter(self.items)

    def __next__(self):
        if self.index < len(self.items):
            result = self.items[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

    @property
    def rgb_values(self) -> tuple:
        return self.r / 255, self.g / 255, self.b / 255

    def __repr__(self):
        return "RGBColor ({}, {}, {})".format(self.r, self.g, self.b)


class TUDColors(object):
    """
    Klasse für die Farben der TU Dresden.
        # HKS 41	0 / 48 / 94 	#00305d - cddarkblue
        # Cyan	    0 / 158 / 224	#009de0 - not defined
        # HKS 92	114 / 120 / 121	#717778 - cdgray
        # HKS 44	0 / 106 / 179	#006ab2 - cdblue
        # HKS 33	147 / 16 / 126 	#93107d - cdpurple
        # HKS 36	84 / 55 / 138	#54368a - cdindigo
        # HKS 65	106 / 176 / 35	#69af22 - cdgreen
        # HKS 57	0 / 125 / 64	#007d3f - cddarkgreen
        # HKS 07	238 / 127 / 0	#ee7f00 - cdorange
    """

    def __init__(self):
        """
        Constructor for the TUDColors class. Initializes the color attributes.
        Each attribute represents RGB values of the color.
        """
        self._cddarkblue = RGBColor(0, 48, 94)
        self._cdgray = RGBColor(114, 120, 121)
        self._cdblue = RGBColor(0, 106, 179)
        self._cdpurple = RGBColor(147, 16, 126)
        self._cdindigo = RGBColor(84, 55, 138)
        self._cdgreen = RGBColor(106, 176, 35)
        self._cddarkgreen = RGBColor(0, 125, 64)
        self._cdorange = RGBColor(238, 127, 0)

    @staticmethod
    def shade_color(color: RGBColor, shade) -> RGBColor:
        """
        Method to shade a color by a given factor.

        Args:
        - color: Tuple with RGB values.
        - shade: Factor to shade the color.

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        white = (255, 255, 255)
        shade = 1 - shade
        new_values = (int(c + (white[i] - c) * shade) for i, c in enumerate(color))
        # new_values = [int(c / shade) for c in color]
        return copy.copy(RGBColor(*new_values))

    def cddarkblue(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cddarkblue' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cddarkblue, shade)

    def cdgray(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cdgray' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cdgray, shade)

    def cdblue(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cdblue' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cdblue, shade)

    def cdpurple(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cdpurple' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cdpurple, shade)

    def cdindigo(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cdindigo' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cdindigo, shade)

    def cdgreen(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cdgreen' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cdgreen, shade)

    def cddarkgreen(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cddarkgreen' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cddarkgreen, shade)

    def cdorange(self, shade=100) -> RGBColor:
        """
        Property that returns the RGB values of the color 'cdorange' shaded by a given factor.

        Args:
        - shade: Factor to shade the color. Default is 100 (no shading).

        Returns:
        - Tuple with RGB values of the shaded color.
        """
        shade = shade / 100
        return self.shade_color(self._cdorange, shade)


# make settings for the plot
mpl.use('pgf')
plt.rcParams.update({
    "pgf.texsystem": "pdflatex",  # use pdflatex backend - usually the case
    "font.family": "serif",  # use serif/main font for text elements
    "text.usetex": True,  # use inline math for ticks
    "pgf.rcfonts": False,  # don't setup fonts from rc parameters
    ## You can change the font size of individual items with:
    # "font.size": 11,
    # "axes.titlesize": 11,
    # "legend.fontsize": 11,
    # "axes.labelsize": 11,
})


# Set the width of the document
def plot_sinus(figurewidth_in,  filename):
    """
    Plots the sinus function and saves it as a pgf and pdf file.

    Args:
    - figurewidth_in (float): Width of the figure in inches.
    - filename (str): Name of the file to save the plot to.
    """
    fig, ax = plt.subplots(figsize=(figurewidth_in, 0.618*figurewidth_in))
    x = np.linspace(-2*np.pi, 2*np.pi, 100)
    y = np.sin(x)

    ax.plot(x, y, label=r'$f(x) = sin(x)$', color=tudcolors.cddarkblue().rgb_values)
    ax.set_title('Sinus-Funktion', pad=20)
    ax.grid(True)  # Ensure grid is visible

    # Adjusting axis labels to be closer to the arrows
    # ax.set_xlabel('x', labelpad=10, loc='right')  # Positioning label at the end
    # ax.set_ylabel('y', labelpad=25, loc='top', rotation=0)  # Positioning label at the end and rotating

    # Verwenden von Text-Objekten für Achsenbeschriftungen
    ax.text(1.1 * np.max(x), -0.15, 'x', ha='right', va='center')  # X-Achsenbeschriftung
    ax.text(0.3, 1.1 * np.max(y), 'y', ha='left', va='center', rotation=0)  # Y-Achsenbeschriftung

    # Hinzufügen der Legende oben rechts
    plt.legend(loc='upper right')

    # Adjusting the tick positions
    ax.spines['left'].set_position(('data', 0))
    ax.spines['left'].set_color(tudcolors.cdgray().rgb_values)
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['bottom'].set_color(tudcolors.cdgray().rgb_values)
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Adding arrows
    ax.plot((1), (0), ls="", marker=">", ms=10, color=tudcolors.cdgray().rgb_values, transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot((0), (1), ls="", marker="^", ms=10, color=tudcolors.cdgray().rgb_values, transform=ax.get_xaxis_transform(), clip_on=False)

    # Adjust tick positions to the left and bottom
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    # Die Farbe der Tick-Labels an den Achsen ändern
    ax.tick_params(axis='x', colors=tudcolors.cdgray().rgb_values)  # Farbe der X-Achsen-Ticks
    ax.tick_params(axis='y', colors=tudcolors.cdgray().rgb_values)  # Farbe der Y-Achsen-Ticks

    # Set x ticks at multiples of pi and apply the custom formatter
    ax.xaxis.set_major_locator(ticker.MultipleLocator(base=np.pi))
    # Define a function to format the x-axis labels as multiples of pi
    def format_func(value, tick_number):
        N = int(np.round(value / np.pi))
        if N == 0:
            return "0"
        elif N == 1:
            return r"$\pi$"
        elif N == -1:
            return r"-$\pi$"
        else:
            return r"${0}\pi$".format(N)
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(format_func))

    fig.tight_layout()

    # Speichern der Plots
    #filename = '{name}.pdf'.format(name=filename)
    fig.savefig(filename, bbox_inches='tight')


# Function to calc figure size
def calc_figsize(width_pt, subplots=(1, 1)):
    """Set figure dimensions to sit nicely in our document.

    Args:
        width_pt (float): Document width in points (1 inch = 72.27 points)
        subplots (tuple): Number of rows and columns of subplots.

    Returns:
        tuple: Figure dimensions in inches.
    """
    ## Variablen
    inches_per_pt = 1 / 72.27
    # Golden ratio to set aesthetic figure height
    golden_ratio = (5 ** .5 - 1) / 2

    ## Berechnung
    # Figure width in inches
    fig_width = width_pt * inches_per_pt
    # Figure height in inches
    fig_height = fig_width * golden_ratio * (subplots[0] / subplots[1])

    ## Rueckgabe
    return fig_width, fig_height


def cmyk_zu_rgb(c: int, m: int, y: int, k: int):
    """
    Konvertiere CMYK Farbwerte in RGB.

    Args:
    - c, m, y, k: CMYK-Werte im Bereich [0, 1].

    Returns:
    - Eine Tuple mit (R, G, B) Werten im Bereich [0, 255].
    """
    r = 255 * (1 - c) * (1 - k)
    g = 255 * (1 - m) * (1 - k)
    b = 255 * (1 - y) * (1 - k)

    return int(r), int(g), int(b)


tudcolors = TUDColors()


if __name__ == '__main__':
    x = calc_figsize(418.25555)
    print(x)
    rgb = cmyk_zu_rgb(0.1, 0, 0.05, 0.65)
    print("RGB:", rgb)

    tudcolors = TUDColors()
    cddarkblue50 = tudcolors.cddarkblue(50)
    cddarkblue = tudcolors.cddarkblue()
