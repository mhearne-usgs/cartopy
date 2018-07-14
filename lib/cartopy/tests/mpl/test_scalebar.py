#!/usr/bin/env python

from cartopy.mpl.scale_bar import ScaleBar
import cartopy.crs as ccrs
import cartopy
import matplotlib.pyplot as plt

# stdlib stuff
import os.path


def test_scalebar_methods():
    xmin, ymin, xmax, ymax = (-121.046000, -116.046000, 32.143500, 36.278500)
    # define desired figure width,height
    figsize = (7, 7)
    clon = (xmin + xmax) / 2
    proj = ccrs.Mercator(central_longitude=clon,
                         globe=None)
    geoproj = ccrs.PlateCarree()
    figure = plt.figure(figsize=figsize)
    ax = figure.add_axes([0, 0, 1, 1], projection=proj)
    ax.set_extent([xmin, xmax, ymin, ymax], crs=geoproj)

    ax.add_feature(cartopy.feature.COASTLINE)

    scale_bar = ScaleBar(ax)

    scale_bar._draw_box()
    scale_bar._draw_divisions()
    scale_bar._draw_ticks()
    scale_bar._draw_labels()
    scale_bar._draw_units()

    testfile = os.path.join(os.path.expanduser('~'), 'cartopy_test1.pdf')
    plt.savefig(testfile)


def test_draw_scalebar():
    xmin, ymin, xmax, ymax = (-121.046000, -116.046000, 32.143500, 36.278500)
    # define desired figure width,height
    figsize = (7, 7)
    clon = (xmin + xmax) / 2
    proj = ccrs.Mercator(central_longitude=clon,
                         globe=None)
    geoproj = ccrs.PlateCarree()
    figure = plt.figure(figsize=figsize)
    ax = figure.add_axes([0, 0, 1, 1], projection=proj)
    ax.set_extent([xmin, xmax, ymin, ymax], crs=geoproj)

    ax.add_feature(cartopy.feature.COASTLINE)

    scale_bar = ScaleBar(ax)

    scale_bar.draw_scalebar()

    testfile = os.path.join(os.path.expanduser('~'), 'cartopy_test2.pdf')
    plt.savefig(testfile)


def test_projections():
    xmin, xmax, ymin, ymax = (-90, -31, -57, 15)
    # define desired figure width,height
    figsize = (7, 7)
    clon = (xmin + xmax) / 2
    clat = (ymin + ymax) / 2

    projections = {'AlbersEqualArea': {'central_longitude': clon,
                                       'central_latitude': clat},
                   'AzimuthalEquidistant': {'central_longitude': clon,
                                            'central_latitude': clat},
                   'LambertConformal': {'central_longitude': clon,
                                        'central_latitude': clat},
                   'LambertCylindrical': {'central_longitude': clon},
                   'Mercator': {'central_longitude': clon,
                                'latitude_true_scale': clat},
                   'Miller': {'central_longitude': clon},
                   'Mollweide': {'central_longitude': clon},
                   'Orthographic': {'central_longitude': clon,
                                    'central_latitude': clat},
                   'PlateCarree': {'central_longitude': clon}}

    for proj_name, proj_params in projections.items():
        proj_class = eval('ccrs.%s' % proj_name)
        proj = proj_class(**proj_params)
        geoproj = ccrs.PlateCarree()
        figure = plt.figure(figsize=figsize)
        ax = figure.add_axes([0, 0, 1, 1], projection=proj)
        ax.add_feature(cartopy.feature.COASTLINE)
        ax.set_extent([xmin, xmax, ymin, ymax], crs=geoproj)
        scale_bar = ScaleBar(ax)
        scale_bar.draw_scalebar()

        fname = 'cartopy_%s.pdf' % proj_name
        testfile = os.path.join(os.path.expanduser('~'), fname)
        plt.savefig(testfile)


if __name__ == '__main__':
    # test_scalebar_methods()
    # test_draw_scalebar()
    test_projections()
