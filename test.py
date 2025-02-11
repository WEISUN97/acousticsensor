import gdsfactory as gf
import Tools.geo_trans as tg

# Create a blank component (essentially an empty GDS cell with some special features)
c = gf.Component()

tg.polygon([(0, 0), (10, 0), (10, 10), (0, 10)])
