# state file generated using paraview version 6.0.0-RC1
import paraview
paraview.compatibility.major = 6
paraview.compatibility.minor = 0

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.Set(
    ViewSize=[1040, 891],
    AxesGrid='Grid Axes 3D Actor',
    CenterOfRotation=[0.17789348307996988, 0.29150959849357605, 0.010571092367172241],
    CameraPosition=[0.18655098589897579, 0.45128901812599265, 0.43556000117823024],
    CameraFocalPoint=[0.18293410912842542, 0.32484716558248083, 0.0008328124188659597],
    CameraViewUp=[0.2578337189024002, 0.9271669326665694, -0.2718147390533182],
    CameraFocalDisk=1.0,
    CameraParallelScale=0.20759502145348147,
    OSPRayMaterialLibrary=materialLibrary1,
)

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1040, 891)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'EnSight Reader'
ensight_dualcase = EnSightReader(registrationName='ensight_dual.case', CaseFileName='C:\\Users\\raw17\\LuisBravo\\Ensight_Dual\\ensight_dual.case')
ensight_dualcase.PointArrays = ['P', 'T', 'U']

# create a new 'Stream Tracer'
streamTracer10 = StreamTracer(registrationName='StreamTracer10', Input=ensight_dualcase,
    SeedType='Line')
streamTracer10.Set(
    Vectors=['POINTS', 'U'],
    MaximumStreamlineLength=1.365440011024475,
)

# init the 'Line' selected for 'SeedType'
streamTracer10.SeedType.Set(
    Point1=[0.106828916470534, 0.336423903910112, 0.0033796421268850285],
    Point2=[0.2570960365736352, 0.3373341495450844, -0.012785542678637383],
)

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=ensight_dualcase)
slice1.Set(
    SliceType='Plane',
    SliceOffsetValues=[0.0],
    PointMergeMethod='Uniform Binning',
)

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Set(
    Origin=[0.1784719536033221, 0.2792370902825771, 0.036175575015790364],
    Normal=[0.8047784259877296, -0.36796125610745706, 0.46576410238288535],
)

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.18272000551223755, 0.2983773648738861, 0.039602989330887794]

# create a new 'Extract Block'
importantBits = ExtractBlock(registrationName='ImportantBits', Input=ensight_dualcase)
importantBits.Set(
    Assembly='Hierarchy',
    Selectors=['/Root/WALL_PILOT', '/Root/WALL_DIFFUSER', '/Root/WALL_LINER_OUTER', '/Root/WALL_LINER_INNER', '/Root/WALL_LINER_CENTERBODY', '/Root/WALL_DILUTION_OUTER', '/Root/WALL_DILUTION_CENTERBODY', '/Root/WALL_DILUTION_INNER', '/Root/WALL_FUEL_MAST', '/Root/S1', '/Root/F2', '/Root/F1', '/Root/A6_INJ', '/Root/A6_EXT', '/Root/A13_INJ', '/Root/A14_INJ', '/Root/A13_EXT', '/Root/A12_INJ', '/Root/A12_EXT', '/Root/A14_EXT', '/Root/A7_INJ', '/Root/A7_EXT', '/Root/A2_INJ', '/Root/A2_EXT', '/Root/A3_INJ', '/Root/A3_EXT', '/Root/A4_INJ', '/Root/A4_EXT', '/Root/A5_EXT', '/Root/A5_INJ', '/Root/A8_INJ', '/Root/A8_EXT', '/Root/A9_INJ', '/Root/A9_EXT', '/Root/A10_INJ', '/Root/A10_EXT', '/Root/A11_INJ', '/Root/A11_EXT', '/Root/WALL_MAIN', '/Root/WALL_MAIN_LIP', '/Root/WALL_PILOT_LIP', '/Root/WALL_DIFFUSER_INTERSECT', '/Root/STATOR1_SUCTION', '/Root/STATOR1_PRESSURE'],
)

# create a new 'Stream Tracer'
streamTracer11 = StreamTracer(registrationName='StreamTracer11', Input=ensight_dualcase,
    SeedType='Line')
streamTracer11.Set(
    Vectors=['POINTS', 'U'],
    MaximumStreamlineLength=1.365440011024475,
)

# init the 'Line' selected for 'SeedType'
streamTracer11.SeedType.Set(
    Point1=[0.13467827199047158, 0.2576225605274937, -0.0006084106399851389],
    Point2=[0.22166943991250918, 0.27116150819336265, -0.0001886508205262167],
)

# create a new 'Stream Tracer'
streamTracer01 = StreamTracer(registrationName='StreamTracer01', Input=ensight_dualcase,
    SeedType='Line')
streamTracer01.Set(
    Vectors=['POINTS', 'U'],
    MaximumStreamlineLength=1.365440011024475,
)

# init the 'Line' selected for 'SeedType'
streamTracer01.SeedType.Set(
    Point1=[0.13602558294987127, 0.2580206880062745, 0.05031739924028099],
    Point2=[0.2378134166231348, 0.2554083059140106, 0.054254659057127466],
)

# create a new 'Tube'
airflow01 = Tube(registrationName='Airflow01', Input=streamTracer01)
airflow01.Set(
    Scalars=['POINTS', 'P'],
    Vectors=['POINTS', 'Normals'],
    Radius=0.0002558112813418575,
)

# create a new 'Glyph'
velocityMarkers01 = Glyph(registrationName='VelocityMarkers01', Input=airflow01,
    GlyphType='Cone')
velocityMarkers01.Set(
    OrientationArray=['POINTS', 'U'],
    ScaleArray=['POINTS', 'U'],
    ScaleFactor=2e-05,
    GlyphTransform='Transform2',
)

# create a new 'Group Datasets'
groupDatasets2 = GroupDatasets(registrationName='GroupDatasets2', Input=[airflow01, velocityMarkers01])
groupDatasets2.BlockNames = ['Airflow01', 'VelocityMarkers01']

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=ensight_dualcase)
threshold2.Set(
    Scalars=['POINTS', 'T'],
    UpperThreshold=2297.0435485839844,
    ThresholdMethod='Above Upper Threshold',
)

# create a new 'Stream Tracer'
streamTracer00 = StreamTracer(registrationName='StreamTracer00', Input=ensight_dualcase,
    SeedType='Line')
streamTracer00.Set(
    Vectors=['POINTS', 'U'],
    MaximumStreamlineLength=1.365440011024475,
)

# init the 'Line' selected for 'SeedType'
streamTracer00.SeedType.Set(
    Point1=[0.1337771256744492, 0.3301426666784453, 0.06933065842658258],
    Point2=[0.24129389931896378, 0.3357703439184768, 0.07422279668547807],
)

# create a new 'Tube'
airflow00 = Tube(registrationName='Airflow00', Input=streamTracer00)
airflow00.Set(
    Scalars=['POINTS', 'P'],
    Vectors=['POINTS', 'Normals'],
    Radius=0.0002558112813418575,
)

# create a new 'Glyph'
velocityMarkers00 = Glyph(registrationName='VelocityMarkers00', Input=airflow00,
    GlyphType='Cone')
velocityMarkers00.Set(
    OrientationArray=['POINTS', 'U'],
    ScaleArray=['POINTS', 'U'],
    ScaleFactor=2e-05,
    GlyphTransform='Transform2',
)

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[airflow00, velocityMarkers00])
groupDatasets1.BlockNames = ['Airflow00', 'VelocityMarkers00']

# create a new 'Extract Block'
noWalls = ExtractBlock(registrationName='NoWalls', Input=ensight_dualcase)
noWalls.Set(
    Assembly='Hierarchy',
    Selectors=['/Root/WALL_PILOT', '/Root/WALL_LINER_CENTERBODY', '/Root/WALL_DILUTION_OUTER', '/Root/WALL_DILUTION_CENTERBODY', '/Root/WALL_DILUTION_INNER', '/Root/WALL_FUEL_MAST', '/Root/S1', '/Root/F2', '/Root/F1', '/Root/A6_INJ', '/Root/A6_EXT', '/Root/A13_INJ', '/Root/A14_INJ', '/Root/A13_EXT', '/Root/A12_INJ', '/Root/A12_EXT', '/Root/A14_EXT', '/Root/A7_INJ', '/Root/A7_EXT', '/Root/A2_INJ', '/Root/A2_EXT', '/Root/A3_INJ', '/Root/A3_EXT', '/Root/A4_INJ', '/Root/A4_EXT', '/Root/A8_INJ', '/Root/A8_EXT', '/Root/A9_INJ', '/Root/A9_EXT', '/Root/A11_INJ', '/Root/A11_EXT', '/Root/WALL_MAIN', '/Root/WALL_MAIN_LIP', '/Root/WALL_PILOT_LIP', '/Root/STATOR1_SUCTION', '/Root/STATOR1_PRESSURE'],
)

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=ensight_dualcase)
clip2.ClipType = 'Plane'

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Set(
    Origin=[0.18930563564501268, 0.2977725263983893, 0.04354865677191074],
    Normal=[0.8551710280942326, -0.07854075168104989, 0.5123610670548934],
)

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [0.18272000551223755, 0.2983773648738861, 0.039602989330887794]

# create a new 'Tube'
airflow11 = Tube(registrationName='Airflow11', Input=streamTracer11)
airflow11.Set(
    Scalars=['POINTS', 'P'],
    Vectors=['POINTS', 'Normals'],
    Radius=0.0002558112813418575,
)

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=ensight_dualcase)
threshold1.Set(
    Scalars=['POINTS', 'T'],
    LowerThreshold=760.0579528808594,
    UpperThreshold=362241.96875,
)

# create a new 'Tube'
airflow10 = Tube(registrationName='Airflow10', Input=streamTracer10)
airflow10.Set(
    Scalars=['POINTS', 'P'],
    Vectors=['POINTS', 'Normals'],
    Radius=0.0002558112813418575,
)

# create a new 'Glyph'
velocityMarkers10 = Glyph(registrationName='VelocityMarkers10', Input=airflow10,
    GlyphType='Cone')
velocityMarkers10.Set(
    OrientationArray=['POINTS', 'U'],
    ScaleArray=['POINTS', 'U'],
    ScaleFactor=2e-05,
    GlyphTransform='Transform2',
)

# create a new 'Group Datasets'
groupDatasets3 = GroupDatasets(registrationName='GroupDatasets3', Input=[airflow10, velocityMarkers10])
groupDatasets3.BlockNames = ['Airflow10', 'VelocityMarkers10']

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=slice1)
clip1.ClipType = 'Plane'

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Set(
    Origin=[0.19678723067045212, 0.29903825372457504, 0.039604149758815765],
    Normal=[0.851977068622833, 0.441851352922751, -0.28089581068641656],
)

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.19678723067045212, 0.29903825372457504, 0.039604149758815765]

# create a new 'Glyph'
velocityMarkers11 = Glyph(registrationName='VelocityMarkers11', Input=airflow11,
    GlyphType='Cone')
velocityMarkers11.Set(
    OrientationArray=['POINTS', 'U'],
    ScaleArray=['POINTS', 'U'],
    ScaleFactor=2e-05,
    GlyphTransform='Transform2',
)

# create a new 'Group Datasets'
groupDatasets4 = GroupDatasets(registrationName='GroupDatasets4', Input=[airflow11, velocityMarkers11])
groupDatasets4.BlockNames = ['Airflow11', 'VelocityMarkers11']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from groupDatasets3
groupDatasets3Display = Show(groupDatasets3, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'T'
tTF2D = GetTransferFunction2D('T')

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')
tLUT.Set(
    TransferFunction2D=tTF2D,
    RGBPoints=[
        # scalar, red, green, blue
        567.934753417969, 0.0564, 0.0564, 0.47,
        897.602793840332, 0.10588235294117647, 0.24705882352941178, 0.6509803921568628,
        897.602793840332, 0.243, 0.46035, 0.81,
        897.602793840332, 0.21176470588235294, 0.5568627450980392, 0.8784313725490196,
        1141.405212726746, 0.356814, 0.745025, 0.954368,
        1281.0300292968755, 0.4980392156862745, 0.8627450980392157, 0.9372549019607843,
        1281.0300292968755, 0.6882, 0.93, 0.91791,
        1375.3236083984375, 0.8, 0.9490196078431372, 0.9294117647058824,
        1546.2308349609375, 0.9490196078431372, 0.9568627450980393, 0.9215686274509803,
        1622.8443603515625, 0.9372549019607843, 0.9568627450980393, 0.8627450980392157,
        1698.0533646905517, 0.899496, 0.944646, 0.768657,
        1698.0533646905517, 0.957108, 0.833819, 0.508916,
        1840.8983154296875, 0.9411764705882353, 0.6980392156862745, 0.3686274509803922,
        1924.59543533722, 0.927521, 0.621439, 0.315357,
        1924.59543533722, 0.8980392156862745, 0.5490196078431373, 0.2627450980392157,
        2123.779052734375, 0.8274509803921568, 0.403921568627451, 0.1803921568627451,
        2196.4478413452152, 0.8, 0.352, 0.16,
        2265.219482421875, 0.7490196078431373, 0.2823529411764706, 0.1450980392156863,
        2424.33984375, 0.6313725490196078, 0.13725490196078433, 0.12549019607843137,
        2489.166748046875, 0.59, 0.0767, 0.119475,
    ],
    ScalarRangeInitialized=1.0,
)

# trace defaults for the display properties.
groupDatasets3Display.Set(
    Representation='Surface',
    ColorArrayName=['POINTS', 'T'],
    LookupTable=tLUT,
    Assembly='Hierarchy',
    DataAxesGrid='Grid Axes Representation',
    PolarAxes='Polar Axes Representation',
)

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
groupDatasets3Display.ScaleTransferFunction.Points = [234541.6875, 0.0, 0.5, 0.0, 338382.0625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
groupDatasets3Display.OpacityTransferFunction.Points = [234541.6875, 0.0, 0.5, 0.0, 338382.0625, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for tLUT in view renderView1
tLUTColorBar = GetScalarBar(tLUT, renderView1)
tLUTColorBar.Set(
    WindowLocation='Upper Right Corner',
    Title='T',
    ComponentTitle='',
)

# set color bar visibility
tLUTColorBar.Visibility = 1

# show color legend
groupDatasets3Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')
tPWF.Set(
    Points=[567.9347534179688, 0.0, 0.5, 0.0, 1893.9384765625, 0.3839285969734192, 0.5, 0.0, 2489.166748046875, 1.0, 0.5, 0.0],
    ScalarRangeInitialized=1,
)

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation scene

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.Set(
    ViewModules=renderView1,
    Cues=timeAnimationCue1,
    AnimationTime=0.2361522388333908,
    StartTime=0.2360678964510326,
    EndTime=0.2361522388333908,
    PlayMode='Snap To TimeSteps',
)

# ----------------------------------------------------------------
# restore active source
SetActiveSource(None)
# ----------------------------------------------------------------


##--------------------------------------------
## You may need to add some code at the end of this python script depending on your usage, eg:
#
## Render all views to see them appears
# RenderAllViews()
#
## Interact with the view, usefull when running from pvpython
# Interact()
#
## Save a screenshot of the active view
# SaveScreenshot("path/to/screenshot.png")
#
## Save a screenshot of a layout (multiple splitted view)
# SaveScreenshot("path/to/screenshot.png", GetLayout())
#
## Save all "Extractors" from the pipeline browser
# SaveExtracts()
#
## Save a animation of the current active view
# SaveAnimation()
#
## Please refer to the documentation of paraview.simple
## https://www.paraview.org/paraview-docs/latest/python/paraview.simple.html
##--------------------------------------------