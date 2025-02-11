import gdsfactory as gf


# create a polygon reference
def polygon(points):
    p = gf.kdb.DPolygon(points)
    return p


# create a region (unit: nm)
def region(p):
    r = gf.kdb.Region(p.to_itype(gf.kcl.dbu))
    return r
