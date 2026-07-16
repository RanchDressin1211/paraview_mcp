# state file generated using paraview version 5.13.3
import paraview
paraview.compatibility.major = 5
paraview.compatibility.minor = 13

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
renderView1.ViewSize = [1560, 662]
renderView1.AxesGrid = 'Grid Axes 3D Actor'
renderView1.CenterOfRotation = [0.17789348307996988, 0.29150959849357605, 0.010571092367172241]
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [0.19307027873969837, 0.011913126701268154, 0.611409020992275]
renderView1.CameraFocalPoint = [0.1778934830799682, 0.2915095984935777, 0.010571092367172855]
renderView1.CameraViewUp = [-0.08954186416598094, -0.9038633778844383, -0.41834584816992554]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 0.20759502145348147
renderView1.LegendGrid = 'Legend Grid Actor'
renderView1.PolarGrid = 'Polar Grid Actor'
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.AssignView(0, renderView1)
layout1.SetSize(1560, 662)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'EnSight Reader'
ensight_dualcase = EnSightReader(registrationName='ensight_dual.case', CaseFileName='C:/Users/raw17/LuisBravo/Ensight_Dual/ensight_dual.case')
ensight_dualcase.PointArrays = ['P', 'T', 'U']

# create a new 'Threshold'
threshold2 = Threshold(registrationName='Threshold2', Input=ensight_dualcase)
threshold2.Scalars = ['POINTS', 'T']
threshold2.LowerThreshold = 202028.0
threshold2.UpperThreshold = 2297.0435485839844
threshold2.ThresholdMethod = 'Above Upper Threshold'

# create a new 'Stream Tracer'
streamTracer11 = StreamTracer(registrationName='StreamTracer11', Input=ensight_dualcase,
    SeedType='Line')
streamTracer11.Vectors = ['POINTS', 'U']
streamTracer11.MaximumStreamlineLength = 1.365440011024475

# init the 'Line' selected for 'SeedType'
streamTracer11.SeedType.Point1 = [0.13467827199047158, 0.2576225605274937, -0.0006084106399851389]
streamTracer11.SeedType.Point2 = [0.22166943991250918, 0.27116150819336265, -0.0001886508205262167]

# create a new 'Tube'
airflow11 = Tube(registrationName='Airflow11', Input=streamTracer11)
airflow11.Scalars = ['POINTS', 'P']
airflow11.Vectors = ['POINTS', 'Normals']
airflow11.Radius = 0.0002558112813418575

# create a new 'Extract Block'
noWalls = ExtractBlock(registrationName='NoWalls', Input=ensight_dualcase)
noWalls.Assembly = 'Hierarchy'
noWalls.Selectors = ['/Root/WALL_PILOT', '/Root/WALL_LINER_CENTERBODY', '/Root/WALL_DILUTION_OUTER', '/Root/WALL_DILUTION_CENTERBODY', '/Root/WALL_DILUTION_INNER', '/Root/WALL_FUEL_MAST', '/Root/S1', '/Root/F2', '/Root/F1', '/Root/A6_INJ', '/Root/A6_EXT', '/Root/A13_INJ', '/Root/A14_INJ', '/Root/A13_EXT', '/Root/A12_INJ', '/Root/A12_EXT', '/Root/A14_EXT', '/Root/A7_INJ', '/Root/A7_EXT', '/Root/A2_INJ', '/Root/A2_EXT', '/Root/A3_INJ', '/Root/A3_EXT', '/Root/A4_INJ', '/Root/A4_EXT', '/Root/A8_INJ', '/Root/A8_EXT', '/Root/A9_INJ', '/Root/A9_EXT', '/Root/A11_INJ', '/Root/A11_EXT', '/Root/WALL_MAIN', '/Root/WALL_MAIN_LIP', '/Root/WALL_PILOT_LIP', '/Root/STATOR1_SUCTION', '/Root/STATOR1_PRESSURE']

# create a new 'Slice'
slice1 = Slice(registrationName='Slice1', Input=ensight_dualcase)
slice1.SliceType = 'Plane'
slice1.HyperTreeGridSlicer = 'Plane'
slice1.SliceOffsetValues = [0.0]
slice1.PointMergeMethod = 'Uniform Binning'

# init the 'Plane' selected for 'SliceType'
slice1.SliceType.Origin = [0.1784719536033221, 0.2792370902825771, 0.036175575015790364]
slice1.SliceType.Normal = [0.8047784259877296, -0.36796125610745706, 0.46576410238288535]

# init the 'Plane' selected for 'HyperTreeGridSlicer'
slice1.HyperTreeGridSlicer.Origin = [0.18272000551223755, 0.2983773648738861, 0.039602989330887794]

# create a new 'Clip'
clip1 = Clip(registrationName='Clip1', Input=slice1)
clip1.ClipType = 'Plane'
clip1.HyperTreeGridClipper = 'Plane'
clip1.Scalars = ['POINTS', 'P']
clip1.Value = 318368.734375

# init the 'Plane' selected for 'ClipType'
clip1.ClipType.Origin = [0.19678723067045212, 0.29903825372457504, 0.039604149758815765]
clip1.ClipType.Normal = [0.851977068622833, 0.441851352922751, -0.28089581068641656]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip1.HyperTreeGridClipper.Origin = [0.19678723067045212, 0.29903825372457504, 0.039604149758815765]

# create a new 'Stream Tracer'
streamTracer00 = StreamTracer(registrationName='StreamTracer00', Input=ensight_dualcase,
    SeedType='Line')
streamTracer00.Vectors = ['POINTS', 'U']
streamTracer00.MaximumStreamlineLength = 1.365440011024475

# init the 'Line' selected for 'SeedType'
streamTracer00.SeedType.Point1 = [0.1337771256744492, 0.3301426666784453, 0.06933065842658258]
streamTracer00.SeedType.Point2 = [0.24129389931896378, 0.3357703439184768, 0.07422279668547807]

# create a new 'Tube'
airflow00 = Tube(registrationName='Airflow00', Input=streamTracer00)
airflow00.Scalars = ['POINTS', 'P']
airflow00.Vectors = ['POINTS', 'Normals']
airflow00.Radius = 0.0002558112813418575

# create a new 'Glyph'
velocityMarkers11 = Glyph(registrationName='VelocityMarkers11', Input=airflow11,
    GlyphType='Cone')
velocityMarkers11.OrientationArray = ['POINTS', 'U']
velocityMarkers11.ScaleArray = ['POINTS', 'U']
velocityMarkers11.ScaleFactor = 2e-05
velocityMarkers11.GlyphTransform = 'Transform2'

# create a new 'Group Datasets'
groupDatasets4 = GroupDatasets(registrationName='GroupDatasets4', Input=[airflow11, velocityMarkers11])
groupDatasets4.BlockNames = ['Airflow11', 'VelocityMarkers11']

# create a new 'Glyph'
velocityMarkers00 = Glyph(registrationName='VelocityMarkers00', Input=airflow00,
    GlyphType='Cone')
velocityMarkers00.OrientationArray = ['POINTS', 'U']
velocityMarkers00.ScaleArray = ['POINTS', 'U']
velocityMarkers00.ScaleFactor = 2e-05
velocityMarkers00.GlyphTransform = 'Transform2'

# create a new 'Group Datasets'
groupDatasets1 = GroupDatasets(registrationName='GroupDatasets1', Input=[airflow00, velocityMarkers00])
groupDatasets1.BlockNames = ['Airflow00', 'VelocityMarkers00']

# create a new 'Stream Tracer'
streamTracer01 = StreamTracer(registrationName='StreamTracer01', Input=ensight_dualcase,
    SeedType='Line')
streamTracer01.Vectors = ['POINTS', 'U']
streamTracer01.MaximumStreamlineLength = 1.365440011024475

# init the 'Line' selected for 'SeedType'
streamTracer01.SeedType.Point1 = [0.13602558294987127, 0.2580206880062745, 0.05031739924028099]
streamTracer01.SeedType.Point2 = [0.2378134166231348, 0.2554083059140106, 0.054254659057127466]

# create a new 'Tube'
airflow01 = Tube(registrationName='Airflow01', Input=streamTracer01)
airflow01.Scalars = ['POINTS', 'P']
airflow01.Vectors = ['POINTS', 'Normals']
airflow01.Radius = 0.0002558112813418575

# create a new 'Glyph'
velocityMarkers01 = Glyph(registrationName='VelocityMarkers01', Input=airflow01,
    GlyphType='Cone')
velocityMarkers01.OrientationArray = ['POINTS', 'U']
velocityMarkers01.ScaleArray = ['POINTS', 'U']
velocityMarkers01.ScaleFactor = 2e-05
velocityMarkers01.GlyphTransform = 'Transform2'

# create a new 'Group Datasets'
groupDatasets2 = GroupDatasets(registrationName='GroupDatasets2', Input=[airflow01, velocityMarkers01])
groupDatasets2.BlockNames = ['Airflow01', 'VelocityMarkers01']

# create a new 'Stream Tracer'
streamTracer10 = StreamTracer(registrationName='StreamTracer10', Input=ensight_dualcase,
    SeedType='Line')
streamTracer10.Vectors = ['POINTS', 'U']
streamTracer10.MaximumStreamlineLength = 1.365440011024475

# init the 'Line' selected for 'SeedType'
streamTracer10.SeedType.Point1 = [0.106828916470534, 0.336423903910112, 0.0033796421268850285]
streamTracer10.SeedType.Point2 = [0.2570960365736352, 0.3373341495450844, -0.012785542678637383]

# create a new 'Tube'
airflow10 = Tube(registrationName='Airflow10', Input=streamTracer10)
airflow10.Scalars = ['POINTS', 'P']
airflow10.Vectors = ['POINTS', 'Normals']
airflow10.Radius = 0.0002558112813418575

# create a new 'Glyph'
velocityMarkers10 = Glyph(registrationName='VelocityMarkers10', Input=airflow10,
    GlyphType='Cone')
velocityMarkers10.OrientationArray = ['POINTS', 'U']
velocityMarkers10.ScaleArray = ['POINTS', 'U']
velocityMarkers10.ScaleFactor = 2e-05
velocityMarkers10.GlyphTransform = 'Transform2'

# create a new 'Group Datasets'
groupDatasets3 = GroupDatasets(registrationName='GroupDatasets3', Input=[airflow10, velocityMarkers10])
groupDatasets3.BlockNames = ['Airflow10', 'VelocityMarkers10']

# create a new 'Threshold'
threshold1 = Threshold(registrationName='Threshold1', Input=ensight_dualcase)
threshold1.Scalars = ['POINTS', 'T']
threshold1.LowerThreshold = 760.0579528808594
threshold1.UpperThreshold = 362241.96875

# create a new 'Clip'
clip2 = Clip(registrationName='Clip2', Input=ensight_dualcase)
clip2.ClipType = 'Plane'
clip2.HyperTreeGridClipper = 'Plane'
clip2.Scalars = ['POINTS', 'P']
clip2.Value = 282134.984375

# init the 'Plane' selected for 'ClipType'
clip2.ClipType.Origin = [0.18930563564501268, 0.2977725263983893, 0.04354865677191074]
clip2.ClipType.Normal = [0.8551710280942326, -0.07854075168104989, 0.5123610670548934]

# init the 'Plane' selected for 'HyperTreeGridClipper'
clip2.HyperTreeGridClipper.Origin = [0.18272000551223755, 0.2983773648738861, 0.039602989330887794]

# create a new 'Extract Block'
importantBits = ExtractBlock(registrationName='ImportantBits', Input=ensight_dualcase)
importantBits.Assembly = 'Hierarchy'
importantBits.Selectors = ['/Root/WALL_PILOT', '/Root/WALL_DIFFUSER', '/Root/WALL_LINER_OUTER', '/Root/WALL_LINER_INNER', '/Root/WALL_LINER_CENTERBODY', '/Root/WALL_DILUTION_OUTER', '/Root/WALL_DILUTION_CENTERBODY', '/Root/WALL_DILUTION_INNER', '/Root/WALL_FUEL_MAST', '/Root/S1', '/Root/F2', '/Root/F1', '/Root/A6_INJ', '/Root/A6_EXT', '/Root/A13_INJ', '/Root/A14_INJ', '/Root/A13_EXT', '/Root/A12_INJ', '/Root/A12_EXT', '/Root/A14_EXT', '/Root/A7_INJ', '/Root/A7_EXT', '/Root/A2_INJ', '/Root/A2_EXT', '/Root/A3_INJ', '/Root/A3_EXT', '/Root/A4_INJ', '/Root/A4_EXT', '/Root/A5_EXT', '/Root/A5_INJ', '/Root/A8_INJ', '/Root/A8_EXT', '/Root/A9_INJ', '/Root/A9_EXT', '/Root/A10_INJ', '/Root/A10_EXT', '/Root/A11_INJ', '/Root/A11_EXT', '/Root/WALL_MAIN', '/Root/WALL_MAIN_LIP', '/Root/WALL_PILOT_LIP', '/Root/WALL_DIFFUSER_INTERSECT', '/Root/STATOR1_SUCTION', '/Root/STATOR1_PRESSURE']

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from importantBits
importantBitsDisplay = Show(importantBits, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'P'
pTF2D = GetTransferFunction2D('P')

# get color transfer function/color map for 'P'
pLUT = GetColorTransferFunction('P')
pLUT.TransferFunction2D = pTF2D
pLUT.RGBPoints = [202028.0, 0.05639999999999999, 0.05639999999999999, 0.47, 229792.2141872571, 0.24300000000000013, 0.4603500000000004, 0.81, 250324.94782608596, 0.3568143826543521, 0.7450246485363142, 0.954367702893722, 271947.9151094544, 0.6882, 0.93, 0.9179099999999999, 282929.71875, 0.8994959551205902, 0.944646394975174, 0.7686567142818399, 297204.9945412882, 0.957107977357604, 0.8338185108985666, 0.5089156299842102, 316284.08332073095, 0.9275207599610714, 0.6214389091739178, 0.31535705838676426, 339178.9898560623, 0.8, 0.3520000000000001, 0.15999999999999998, 363831.4375, 0.59, 0.07670000000000013, 0.11947499999999994]
pLUT.ColorSpace = 'RGB'
pLUT.NanColor = [0.0, 1.0, 0.0]
pLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
importantBitsDisplay.Representation = 'Surface'
importantBitsDisplay.ColorArrayName = ['POINTS', 'P']
importantBitsDisplay.LookupTable = pLUT
importantBitsDisplay.SelectNormalArray = 'None'
importantBitsDisplay.SelectTangentArray = 'None'
importantBitsDisplay.SelectTCoordArray = 'None'
importantBitsDisplay.TextureTransform = 'Transform2'
importantBitsDisplay.OSPRayScaleArray = 'P'
importantBitsDisplay.OSPRayScaleFunction = 'Piecewise Function'
importantBitsDisplay.Assembly = 'Hierarchy'
importantBitsDisplay.SelectOrientationVectors = 'U'
importantBitsDisplay.ScaleFactor = 0.015605459362268448
importantBitsDisplay.SelectScaleArray = 'P'
importantBitsDisplay.GlyphType = 'Arrow'
importantBitsDisplay.GlyphTableIndexArray = 'P'
importantBitsDisplay.GaussianRadius = 0.0007802729681134224
importantBitsDisplay.SetScaleArray = ['POINTS', 'P']
importantBitsDisplay.ScaleTransferFunction = 'Piecewise Function'
importantBitsDisplay.OpacityArray = ['POINTS', 'P']
importantBitsDisplay.OpacityTransferFunction = 'Piecewise Function'
importantBitsDisplay.DataAxesGrid = 'Grid Axes Representation'
importantBitsDisplay.PolarAxes = 'Polar Axes Representation'
importantBitsDisplay.SelectInputVectors = ['POINTS', 'U']
importantBitsDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
importantBitsDisplay.OpacityTransferFunction.Points = [303840.3125, 0.0, 0.5, 0.0, 335809.21875, 1.0, 0.5, 0.0]

# show data from noWalls
noWallsDisplay = Show(noWalls, renderView1, 'UnstructuredGridRepresentation')

# get opacity transfer function/opacity map for 'P'
pPWF = GetOpacityTransferFunction('P')
pPWF.Points = [202028.0, 0.0, 0.5, 0.0, 363831.4375, 1.0, 0.5, 0.0]
pPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
noWallsDisplay.Representation = 'Surface'
noWallsDisplay.ColorArrayName = ['POINTS', 'P']
noWallsDisplay.LookupTable = pLUT
noWallsDisplay.SelectNormalArray = 'None'
noWallsDisplay.SelectTangentArray = 'None'
noWallsDisplay.SelectTCoordArray = 'None'
noWallsDisplay.TextureTransform = 'Transform2'
noWallsDisplay.OSPRayScaleArray = 'P'
noWallsDisplay.OSPRayScaleFunction = 'Piecewise Function'
noWallsDisplay.Assembly = 'Hierarchy'
noWallsDisplay.SelectedBlockSelectors = ['']
noWallsDisplay.SelectOrientationVectors = 'U'
noWallsDisplay.ScaleFactor = 0.02809441387653351
noWallsDisplay.SelectScaleArray = 'P'
noWallsDisplay.GlyphType = 'Arrow'
noWallsDisplay.GlyphTableIndexArray = 'P'
noWallsDisplay.GaussianRadius = 0.0014047206938266755
noWallsDisplay.SetScaleArray = ['POINTS', 'P']
noWallsDisplay.ScaleTransferFunction = 'Piecewise Function'
noWallsDisplay.OpacityArray = ['POINTS', 'P']
noWallsDisplay.OpacityTransferFunction = 'Piecewise Function'
noWallsDisplay.DataAxesGrid = 'Grid Axes Representation'
noWallsDisplay.PolarAxes = 'Polar Axes Representation'
noWallsDisplay.ScalarOpacityFunction = pPWF
noWallsDisplay.ScalarOpacityUnitDistance = 0.00298553973674471
noWallsDisplay.OpacityArrayName = ['POINTS', 'P']
noWallsDisplay.SelectInputVectors = ['POINTS', 'U']
noWallsDisplay.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
noWallsDisplay.ScaleTransferFunction.Points = [205271.4375, 0.0, 0.5, 0.0, 341571.90625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
noWallsDisplay.OpacityTransferFunction.Points = [205271.4375, 0.0, 0.5, 0.0, 341571.90625, 1.0, 0.5, 0.0]

# show data from groupDatasets1
groupDatasets1Display = Show(groupDatasets1, renderView1, 'GeometryRepresentation')

# get 2D transfer function for 'T'
tTF2D = GetTransferFunction2D('T')

# get color transfer function/color map for 'T'
tLUT = GetColorTransferFunction('T')
tLUT.TransferFunction2D = tTF2D
tLUT.RGBPoints = [567.934753417969, 0.0564, 0.0564, 0.47, 897.602793840332, 0.10588235294117647, 0.24705882352941178, 0.6509803921568628, 897.602793840332, 0.243, 0.46035, 0.81, 897.602793840332, 0.21176470588235294, 0.5568627450980392, 0.8784313725490196, 1141.405212726746, 0.356814, 0.745025, 0.954368, 1281.0300292968755, 0.4980392156862745, 0.8627450980392157, 0.9372549019607843, 1281.0300292968755, 0.6882, 0.93, 0.91791, 1375.3236083984375, 0.8, 0.9490196078431372, 0.9294117647058824, 1546.2308349609375, 0.9490196078431372, 0.9568627450980393, 0.9215686274509803, 1622.8443603515625, 0.9372549019607843, 0.9568627450980393, 0.8627450980392157, 1698.0533646905517, 0.899496, 0.944646, 0.768657, 1698.0533646905517, 0.957108, 0.833819, 0.508916, 1840.8983154296875, 0.9411764705882353, 0.6980392156862745, 0.3686274509803922, 1924.59543533722, 0.927521, 0.621439, 0.315357, 1924.59543533722, 0.8980392156862745, 0.5490196078431373, 0.2627450980392157, 2123.779052734375, 0.8274509803921568, 0.403921568627451, 0.1803921568627451, 2196.4478413452152, 0.8, 0.352, 0.16, 2265.219482421875, 0.7490196078431373, 0.2823529411764706, 0.1450980392156863, 2424.33984375, 0.6313725490196078, 0.13725490196078433, 0.12549019607843137, 2489.166748046875, 0.59, 0.0767, 0.119475]
tLUT.NanColor = [0.0, 1.0, 0.0]
tLUT.ScalarRangeInitialized = 1.0

# trace defaults for the display properties.
groupDatasets1Display.Representation = 'Surface'
groupDatasets1Display.ColorArrayName = ['POINTS', 'T']
groupDatasets1Display.LookupTable = tLUT
groupDatasets1Display.SelectNormalArray = 'None'
groupDatasets1Display.SelectTangentArray = 'None'
groupDatasets1Display.SelectTCoordArray = 'None'
groupDatasets1Display.TextureTransform = 'Transform2'
groupDatasets1Display.OSPRayScaleArray = 'P'
groupDatasets1Display.OSPRayScaleFunction = 'Piecewise Function'
groupDatasets1Display.Assembly = 'Hierarchy'
groupDatasets1Display.SelectedBlockSelectors = ['']
groupDatasets1Display.SelectOrientationVectors = 'Normals'
groupDatasets1Display.ScaleFactor = 0.039631003886461263
groupDatasets1Display.SelectScaleArray = 'P'
groupDatasets1Display.GlyphType = 'Arrow'
groupDatasets1Display.GlyphTableIndexArray = 'P'
groupDatasets1Display.GaussianRadius = 0.0019815501943230627
groupDatasets1Display.SetScaleArray = ['POINTS', 'P']
groupDatasets1Display.ScaleTransferFunction = 'Piecewise Function'
groupDatasets1Display.OpacityArray = ['POINTS', 'P']
groupDatasets1Display.OpacityTransferFunction = 'Piecewise Function'
groupDatasets1Display.DataAxesGrid = 'Grid Axes Representation'
groupDatasets1Display.PolarAxes = 'Polar Axes Representation'
groupDatasets1Display.SelectInputVectors = ['POINTS', 'Normals']
groupDatasets1Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
groupDatasets1Display.ScaleTransferFunction.Points = [226642.9375, 0.0, 0.5, 0.0, 340668.90625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
groupDatasets1Display.OpacityTransferFunction.Points = [226642.9375, 0.0, 0.5, 0.0, 340668.90625, 1.0, 0.5, 0.0]

# show data from groupDatasets2
groupDatasets2Display = Show(groupDatasets2, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
groupDatasets2Display.Representation = 'Surface'
groupDatasets2Display.ColorArrayName = ['POINTS', 'T']
groupDatasets2Display.LookupTable = tLUT
groupDatasets2Display.SelectNormalArray = 'None'
groupDatasets2Display.SelectTangentArray = 'None'
groupDatasets2Display.SelectTCoordArray = 'None'
groupDatasets2Display.TextureTransform = 'Transform2'
groupDatasets2Display.OSPRayScaleArray = 'P'
groupDatasets2Display.OSPRayScaleFunction = 'Piecewise Function'
groupDatasets2Display.Assembly = 'Hierarchy'
groupDatasets2Display.SelectedBlockSelectors = ['']
groupDatasets2Display.SelectOrientationVectors = 'Normals'
groupDatasets2Display.ScaleFactor = 0.03689043966587633
groupDatasets2Display.SelectScaleArray = 'P'
groupDatasets2Display.GlyphType = 'Arrow'
groupDatasets2Display.GlyphTableIndexArray = 'P'
groupDatasets2Display.GaussianRadius = 0.0018445219832938164
groupDatasets2Display.SetScaleArray = ['POINTS', 'P']
groupDatasets2Display.ScaleTransferFunction = 'Piecewise Function'
groupDatasets2Display.OpacityArray = ['POINTS', 'P']
groupDatasets2Display.OpacityTransferFunction = 'Piecewise Function'
groupDatasets2Display.DataAxesGrid = 'Grid Axes Representation'
groupDatasets2Display.PolarAxes = 'Polar Axes Representation'
groupDatasets2Display.SelectInputVectors = ['POINTS', 'Normals']
groupDatasets2Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
groupDatasets2Display.ScaleTransferFunction.Points = [214053.53125, 0.0, 0.5, 0.0, 344956.5, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
groupDatasets2Display.OpacityTransferFunction.Points = [214053.53125, 0.0, 0.5, 0.0, 344956.5, 1.0, 0.5, 0.0]

# show data from groupDatasets4
groupDatasets4Display = Show(groupDatasets4, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
groupDatasets4Display.Representation = 'Surface'
groupDatasets4Display.ColorArrayName = ['POINTS', 'T']
groupDatasets4Display.LookupTable = tLUT
groupDatasets4Display.SelectNormalArray = 'None'
groupDatasets4Display.SelectTangentArray = 'None'
groupDatasets4Display.SelectTCoordArray = 'None'
groupDatasets4Display.TextureTransform = 'Transform2'
groupDatasets4Display.OSPRayScaleArray = 'P'
groupDatasets4Display.OSPRayScaleFunction = 'Piecewise Function'
groupDatasets4Display.Assembly = 'Hierarchy'
groupDatasets4Display.SelectedBlockSelectors = ['']
groupDatasets4Display.SelectOrientationVectors = 'Normals'
groupDatasets4Display.ScaleFactor = 0.03641012756852433
groupDatasets4Display.SelectScaleArray = 'P'
groupDatasets4Display.GlyphType = 'Arrow'
groupDatasets4Display.GlyphTableIndexArray = 'P'
groupDatasets4Display.GaussianRadius = 0.0018205063784262165
groupDatasets4Display.SetScaleArray = ['POINTS', 'P']
groupDatasets4Display.ScaleTransferFunction = 'Piecewise Function'
groupDatasets4Display.OpacityArray = ['POINTS', 'P']
groupDatasets4Display.OpacityTransferFunction = 'Piecewise Function'
groupDatasets4Display.DataAxesGrid = 'Grid Axes Representation'
groupDatasets4Display.PolarAxes = 'Polar Axes Representation'
groupDatasets4Display.SelectInputVectors = ['POINTS', 'Normals']
groupDatasets4Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
groupDatasets4Display.ScaleTransferFunction.Points = [222774.453125, 0.0, 0.5, 0.0, 343042.53125, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
groupDatasets4Display.OpacityTransferFunction.Points = [222774.453125, 0.0, 0.5, 0.0, 343042.53125, 1.0, 0.5, 0.0]

# show data from groupDatasets3
groupDatasets3Display = Show(groupDatasets3, renderView1, 'GeometryRepresentation')

# trace defaults for the display properties.
groupDatasets3Display.Representation = 'Surface'
groupDatasets3Display.ColorArrayName = ['POINTS', 'T']
groupDatasets3Display.LookupTable = tLUT
groupDatasets3Display.SelectNormalArray = 'None'
groupDatasets3Display.SelectTangentArray = 'None'
groupDatasets3Display.SelectTCoordArray = 'None'
groupDatasets3Display.TextureTransform = 'Transform2'
groupDatasets3Display.OSPRayScaleArray = 'P'
groupDatasets3Display.OSPRayScaleFunction = 'Piecewise Function'
groupDatasets3Display.Assembly = 'Hierarchy'
groupDatasets3Display.SelectedBlockSelectors = ['']
groupDatasets3Display.SelectOrientationVectors = 'Normals'
groupDatasets3Display.ScaleFactor = 0.036842561839148406
groupDatasets3Display.SelectScaleArray = 'P'
groupDatasets3Display.GlyphType = 'Arrow'
groupDatasets3Display.GlyphTableIndexArray = 'P'
groupDatasets3Display.GaussianRadius = 0.0018421280919574201
groupDatasets3Display.SetScaleArray = ['POINTS', 'P']
groupDatasets3Display.ScaleTransferFunction = 'Piecewise Function'
groupDatasets3Display.OpacityArray = ['POINTS', 'P']
groupDatasets3Display.OpacityTransferFunction = 'Piecewise Function'
groupDatasets3Display.DataAxesGrid = 'Grid Axes Representation'
groupDatasets3Display.PolarAxes = 'Polar Axes Representation'
groupDatasets3Display.SelectInputVectors = ['POINTS', 'Normals']
groupDatasets3Display.WriteLog = ''

# init the 'Piecewise Function' selected for 'ScaleTransferFunction'
groupDatasets3Display.ScaleTransferFunction.Points = [234541.6875, 0.0, 0.5, 0.0, 338382.0625, 1.0, 0.5, 0.0]

# init the 'Piecewise Function' selected for 'OpacityTransferFunction'
groupDatasets3Display.OpacityTransferFunction.Points = [234541.6875, 0.0, 0.5, 0.0, 338382.0625, 1.0, 0.5, 0.0]

# setup the color legend parameters for each legend in this view

# get color legend/bar for pLUT in view renderView1
pLUTColorBar = GetScalarBar(pLUT, renderView1)
pLUTColorBar.WindowLocation = 'Any Location'
pLUTColorBar.Position = [0.00722733245729304, 0.6622222222222223]
pLUTColorBar.Title = 'P'
pLUTColorBar.ComponentTitle = ''
pLUTColorBar.ScalarBarLength = 0.32999999999999985

# set color bar visibility
pLUTColorBar.Visibility = 1

# get color legend/bar for tLUT in view renderView1
tLUTColorBar = GetScalarBar(tLUT, renderView1)
tLUTColorBar.WindowLocation = 'Upper Right Corner'
tLUTColorBar.Position = [0.9031719532554258, 0.6555555555555556]
tLUTColorBar.Title = 'T'
tLUTColorBar.ComponentTitle = ''

# set color bar visibility
tLUTColorBar.Visibility = 1

# show color legend
importantBitsDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
noWallsDisplay.SetScalarBarVisibility(renderView1, True)

# show color legend
groupDatasets1Display.SetScalarBarVisibility(renderView1, True)

# show color legend
groupDatasets2Display.SetScalarBarVisibility(renderView1, True)

# show color legend
groupDatasets4Display.SetScalarBarVisibility(renderView1, True)

# show color legend
groupDatasets3Display.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup color maps and opacity maps used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'T'
tPWF = GetOpacityTransferFunction('T')
tPWF.Points = [567.9347534179688, 0.0, 0.5, 0.0, 1893.9384765625, 0.3839285969734192, 0.5, 0.0, 2489.166748046875, 1.0, 0.5, 0.0]
tPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# setup animation scene, tracks and keyframes
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get the time-keeper
timeKeeper1 = GetTimeKeeper()

# initialize the timekeeper

# get time animation track
timeAnimationCue1 = GetTimeTrack()

# initialize the animation track

# get animation scene
animationScene1 = GetAnimationScene()

# initialize the animation scene
animationScene1.ViewModules = renderView1
animationScene1.Cues = timeAnimationCue1
animationScene1.AnimationTime = 0.2361522388333908
animationScene1.StartTime = 0.2360678964510326
animationScene1.EndTime = 0.2361522388333908
animationScene1.PlayMode = 'Snap To TimeSteps'
animationScene1.NumberOfFrames = 1

# initialize the animation scene

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