import gdsfactory as gf
import gdsfactory as gf
from gdsfactory.cross_section import ComponentAlongPath

# Create our first CrossSection
s0 = gf.Section(width=1.2, offset=0, layer=(2, 0), name="core", port_names=("o1", "o2"))
s1 = gf.Section(width=2.2, offset=0, layer=(3, 0), name="etch")
s2 = gf.Section(width=1.1, offset=1, layer=(1, 0), name="wg2")
X1 = gf.CrossSection(sections=[s0, s1, s2])

# Create the second CrossSection that we want to transition to
s0 = gf.Section(width=1, offset=0, layer=(2, 0), name="core", port_names=("o1", "o2"))
s1 = gf.Section(width=3.5, offset=0, layer=(3, 0), name="etch")
s2 = gf.Section(width=3, offset=5, layer=(1, 0), name="wg2")
X2 = gf.CrossSection(sections=[s0, s1, s2])

# To show the cross-sections, let's create two Paths and
# create Components by extruding them
P1 = gf.path.straight(length=5)
P2 = gf.path.straight(length=5)
wg1 = gf.path.extrude(P1, X1)
wg2 = gf.path.extrude(P2, X2)

# Place both cross-section Components and quickplot them
c = gf.Component()
wg1ref = c << wg1
wg2ref = c << wg2
wg2ref.movex(7.5)


c.show()
