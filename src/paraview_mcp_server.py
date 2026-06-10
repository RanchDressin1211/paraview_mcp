@mcp.tool()
def edit_source(name: str, source_type: str = None, **kwargs) -> str:
    """
    Edit properties of an existing geometric source.
    
    Args:
        name: The registered name of the source to edit
        source_type: Type of source (Sphere, Cone, Cylinder, Plane, Box) - if changing type, note this may require recreation
        **kwargs: Source-specific properties to edit (e.g., center, radius for Sphere)
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the source with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties based on source type and provided kwargs
        edited_props = []
        
        # Handle type change if requested (note: this may not work for all types)
        if source_type:
            source_type = source_type.lower()
            if hasattr(proxy_to_edit, 'SetSourceType'):
                try:
                    proxy_to_edit.SetSourceType(source_type)
                    edited_props.append(f"type to {source_type}")
                except:
                    return f"Cannot change source type to {source_type}. Consider deleting and recreating."
        
        # Edit common properties
        if 'center' in kwargs:
            center = kwargs['center']
            if hasattr(proxy_to_edit, 'Center'):
                proxy_to_edit.Center = center
                edited_props.append(f"center to {center}")
        
        # Sphere-specific properties
        if source_type == "sphere" or (hasattr(proxy_to_edit, '__class__') and 'Sphere' in proxy_to_edit.__class__.__name__):
            if 'radius' in kwargs:
                radius = kwargs['radius']
                if hasattr(proxy_to_edit, 'Radius'):
                    proxy_to_edit.Radius = radius
                    edited_props.append(f"radius to {radius}")
            if 'theta_resolution' in kwargs:
                theta_res = kwargs['theta_resolution']
                if hasattr(proxy_to_edit, 'ThetaResolution'):
                    proxy_to_edit.ThetaResolution = theta_res
                    edited_props.append(f"theta resolution to {theta_res}")
            if 'phi_resolution' in kwargs:
                phi_res = kwargs['phi_resolution']
                if hasattr(proxy_to_edit, 'PhiResolution'):
                    proxy_to_edit.PhiResolution = phi_res
                    edited_props.append(f"phi resolution to {phi_res}")
        
        # Cone-specific properties
        elif source_type == "cone" or (hasattr(proxy_to_edit, '__class__') and 'Cone' in proxy_to_edit.__class__.__name__):
            if 'radius' in kwargs:
                radius = kwargs['radius']
                if hasattr(proxy_to_edit, 'Radius'):
                    proxy_to_edit.Radius = radius
                    edited_props.append(f"radius to {radius}")
            if 'height' in kwargs:
                height = kwargs['height']
                if hasattr(proxy_to_edit, 'Height'):
                    proxy_to_edit.Height = height
                    edited_props.append(f"height to {height}")
            if 'resolution' in kwargs:
                resolution = kwargs['resolution']
                if hasattr(proxy_to_edit, 'Resolution'):
                    proxy_to_edit.Resolution = resolution
                    edited_props.append(f"resolution to {resolution}")
        
        # Cylinder-specific properties
        elif source_type == "cylinder" or (hasattr(proxy_to_edit, '__class__') and 'Cylinder' in proxy_to_edit.__class__.__name__):
            if 'radius' in kwargs:
                radius = kwargs['radius']
                if hasattr(proxy_to_edit, 'Radius'):
                    proxy_to_edit.Radius = radius
                    edited_props.append(f"radius to {radius}")
            if 'height' in kwargs:
                height = kwargs['height']
                if hasattr(proxy_to_edit, 'Height'):
                    proxy_to_edit.Height = height
                    edited_props.append(f"height to {height}")
            if 'resolution' in kwargs:
                resolution = kwargs['resolution']
                if hasattr(proxy_to_edit, 'Resolution'):
                    proxy_to_edit.Resolution = resolution
                    edited_props.append(f"resolution to {resolution}")
        
        # Plane-specific properties
        elif source_type == "plane" or (hasattr(proxy_to_edit, '__class__') and 'Plane' in proxy_to_edit.__class__.__name__):
            if 'origin' in kwargs:
                origin = kwargs['origin']
                if hasattr(proxy_to_edit, 'Origin'):
                    proxy_to_edit.Origin = origin
                    edited_props.append(f"origin to {origin}")
            if 'point1' in kwargs:
                point1 = kwargs['point1']
                if hasattr(proxy_to_edit, 'Point1'):
                    proxy_to_edit.Point1 = point1
                    edited_props.append(f"point1 to {point1}")
            if 'point2' in kwargs:
                point2 = kwargs['point2']
                if hasattr(proxy_to_edit, 'Point2'):
                    proxy_to_edit.Point2 = point2
                    edited_props.append(f"point2 to {point2}")
            if 'x_resolution' in kwargs:
                x_res = kwargs['x_resolution']
                if hasattr(proxy_to_edit, 'XResolution'):
                    proxy_to_edit.XResolution = x_res
                    edited_props.append(f"x resolution to {x_res}")
            if 'y_resolution' in kwargs:
                y_res = kwargs['y_resolution']
                if hasattr(proxy_to_edit, 'YResolution'):
                    proxy_to_edit.YResolution = y_res
                    edited_props.append(f"y resolution to {y_res}")
        
        # Box-specific properties
        elif source_type == "box" or (hasattr(proxy_to_edit, '__class__') and 'Box' in proxy_to_edit.__class__.__name__):
            if 'bounds' in kwargs:
                bounds = kwargs['bounds']
                if hasattr(proxy_to_edit, 'Bounds'):
                    proxy_to_edit.Bounds = bounds
                    edited_props.append(f"bounds to {bounds}")
            if 'x_length' in kwargs:
                x_length = kwargs['x_length']
                if hasattr(proxy_to_edit, 'XLength'):
                    proxy_to_edit.XLength = x_length
                    edited_props.append(f"x length to {x_length}")
            if 'y_length' in kwargs:
                y_length = kwargs['y_length']
                if hasattr(proxy_to_edit, 'YLength'):
                    proxy_to_edit.YLength = y_length
                    edited_props.append(f"y length to {y_length}")
            if 'z_length' in kwargs:
                z_length = kwargs['z_length']
                if hasattr(proxy_to_edit, 'ZLength'):
                    proxy_to_edit.ZLength = z_length
                    edited_props.append(f"z length to {z_length}")
        
        if edited_props:
            return f"Edited source '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for source '{name}'."
            
    except Exception as e:
        return f"Error editing source: {str(e)}"

@mcp.tool()
def edit_isosurface(name: str, value: float = None, field: str = None) -> str:
    """
    Edit an existing isosurface visualization.
    
    Args:
        name: The registered name of the isosurface to edit
        value: New isovalue
        field: New field name to contour by
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the isosurface with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if value is not None:
            if hasattr(proxy_to_edit, 'Isosurfaces'):
                proxy_to_edit.Isosurfaces = [value]
                edited_props.append(f"isovalue to {value}")
        
        if field is not None:
            if hasattr(proxy_to_edit, 'ContourBy'):
                proxy_to_edit.ContourBy = ['POINTS', field]
                edited_props.append(f"field to {field}")
        
        if edited_props:
            return f"Edited isosurface '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for isosurface '{name}'."
            
    except Exception as e:
        return f"Error editing isosurface: {str(e)}"

@mcp.tool()
def edit_slice(name: str, origin_x: float = None, origin_y: float = None, origin_z: float = None,
               normal_x: float = None, normal_y: float = None, normal_z: float = None) -> str:
    """
    Edit an existing slice visualization.
    
    Args:
        name: The registered name of the slice to edit
        origin_x, origin_y, origin_z: New coordinates for slice plane origin
        normal_x, normal_y, normal_z: New normal vector for slice plane
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the slice with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if origin_x is not None or origin_y is not None or origin_z is not None:
            origin = []
            if origin_x is not None:
                origin.append(origin_x)
            else:
                # Get current value if not provided
                if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Origin'):
                    origin.append(proxy_to_edit.SliceType.Origin[0])
                else:
                    origin.append(0.0)
            
            if origin_y is not None:
                origin.append(origin_y)
            else:
                if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Origin'):
                    origin.append(proxy_to_edit.SliceType.Origin[1])
                else:
                    origin.append(0.0)
                    
            if origin_z is not None:
                origin.append(origin_z)
            else:
                if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Origin'):
                    origin.append(proxy_to_edit.SliceType.Origin[2])
                else:
                    origin.append(0.0)
            
            if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Origin'):
                proxy_to_edit.SliceType.Origin = origin
                edited_props.append(f"origin to {origin}")
        
        if normal_x is not None or normal_y is not None or normal_z is not None:
            normal = []
            if normal_x is not None:
                normal.append(normal_x)
            else:
                if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Normal'):
                    normal.append(proxy_to_edit.SliceType.Normal[0])
                else:
                    normal.append(0.0)
            
            if normal_y is not None:
                normal.append(normal_y)
            else:
                if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Normal'):
                    normal.append(proxy_to_edit.SliceType.Normal[1])
                else:
                    normal.append(0.0)
                    
            if normal_z is not None:
                normal.append(normal_z)
            else:
                if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Normal'):
                    normal.append(proxy_to_edit.SliceType.Normal[2])
                else:
                    normal.append(0.0)
            
            if hasattr(proxy_to_edit, 'SliceType') and hasattr(proxy_to_edit.SliceType, 'Normal'):
                proxy_to_edit.SliceType.Normal = normal
                edited_props.append(f"normal to {normal}")
        
        if edited_props:
            return f"Edited slice '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for slice '{name}'."
            
    except Exception as e:
        return f"Error editing slice: {str(e)}"

@mcp.tool()
def edit_clip(name: str, origin_x: float = None, origin_y: float = None, origin_z: float = None,
              normal_x: float = None, normal_y: float = None, normal_z: float = None,
              invert: bool = None) -> str:
    """
    Edit an existing clip filter.
    
    Args:
        name: The registered name of the clip to edit
        origin_x, origin_y, origin_z: New coordinates for clip plane origin
        normal_x, normal_y, normal_z: New normal vector for clip plane
        invert: New invert flag (True/False)
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the clip with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if origin_x is not None or origin_y is not None or origin_z is not None:
            origin = []
            if origin_x is not None:
                origin.append(origin_x)
            else:
                if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Origin'):
                    origin.append(proxy_to_edit.ClipType.Origin[0])
                else:
                    origin.append(0.0)
            
            if origin_y is not None:
                origin.append(origin_y)
            else:
                if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Origin'):
                    origin.append(proxy_to_edit.ClipType.Origin[1])
                else:
                    origin.append(0.0)
                    
            if origin_z is not None:
                origin.append(origin_z)
            else:
                if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Origin'):
                    origin.append(proxy_to_edit.ClipType.Origin[2])
                else:
                    origin.append(0.0)
            
            if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Origin'):
                proxy_to_edit.ClipType.Origin = origin
                edited_props.append(f"origin to {origin}")
        
        if normal_x is not None or normal_y is not None or normal_z is not None:
            normal = []
            if normal_x is not None:
                normal.append(normal_x)
            else:
                if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Normal'):
                    normal.append(proxy_to_edit.ClipType.Normal[0])
                else:
                    normal.append(0.0)
            
            if normal_y is not None:
                normal.append(normal_y)
            else:
                if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Normal'):
                    normal.append(proxy_to_edit.ClipType.Normal[1])
                else:
                    normal.append(0.0)
                    
            if normal_z is not None:
                normal.append(normal_z)
            else:
                if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Normal'):
                    normal.append(proxy_to_edit.ClipType.Normal[2])
                else:
                    normal.append(0.0)
            
            if hasattr(proxy_to_edit, 'ClipType') and hasattr(proxy_to_edit.ClipType, 'Normal'):
                proxy_to_edit.ClipType.Normal = normal
                edited_props.append(f"normal to {normal}")
        
        if invert is not None:
            if hasattr(proxy_to_edit, 'Invert'):
                proxy_to_edit.Invert = invert
                edited_props.append(f"invert to {invert}")
        
        if edited_props:
            return f"Edited clip '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for clip '{name}'."
            
    except Exception as e:
        return f"Error editing clip: {str(e)}"

@mcp.tool()
def edit_streamline(name: str, seed_point_number: int = None, vector_field: str = None,
                    integration_direction: str = None, max_steps: int = None,
                    initial_step: float = None, maximum_step: float = None,
                    tube_radius: float = None) -> str:
    """
    Edit an existing streamline visualization.
    
    Args:
        name: The registered name of the streamline to edit
        seed_point_number: New number of seed points
        vector_field: New vector field name
        integration_direction: New integration direction ("FORWARD", "BACKWARD", "BOTH")
        max_steps: New maximum number of integration steps
        initial_step: New initial integration step length
        maximum_step: New maximum streamline length
        tube_radius: New tube radius for visualization
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the streamline with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if seed_point_number is not None:
            # For stream tracers, this would be in the seed type
            if hasattr(proxy_to_edit, 'SeedType') and hasattr(proxy_to_edit.SeedType, 'NumberOfPoints'):
                proxy_to_edit.SeedType.NumberOfPoints = seed_point_number
                edited_props.append(f"seed point number to {seed_point_number}")
        
        if vector_field is not None:
            if hasattr(proxy_to_edit, 'Vectors'):
                proxy_to_edit.Vectors = ['POINTS', vector_field]
                edited_props.append(f"vector field to {vector_field}")
        
        if integration_direction is not None:
            if hasattr(proxy_to_edit, 'IntegrationDirection'):
                proxy_to_edit.IntegrationDirection = integration_direction
                edited_props.append(f"integration direction to {integration_direction}")
        
        if max_steps is not None:
            # Note: max_steps is ignored in the underlying implementation
            # which uses number_of_streamlines instead
            pass
        
        if initial_step is not None:
            if hasattr(proxy_to_edit, 'InitialStepLength'):
                proxy_to_edit.InitialStepLength = initial_step
                edited_props.append(f"initial step length to {initial_step}")
        
        if maximum_step is not None:
            if hasattr(proxy_to_edit, 'MaximumStreamlineLength'):
                proxy_to_edit.MaximumStreamlineLength = maximum_step
                edited_props.append(f"maximum streamline length to {maximum_step}")
        
        if tube_radius is not None:
            # Tube radius would be on the tube filter, not the stream tracer directly
            # This would require finding the associated tube filter
            edited_props.append("tube radius (requires editing associated tube filter separately)")
        
        if edited_props:
            return f"Edited streamline '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for streamline '{name}'."
            
    except Exception as e:
        return f"Error editing streamline: {str(e)}"

@mcp.tool()
def edit_filter(name: str, filter_type: str = None, field_name: str = None,
                min_value: float = None, max_value: float = None,
                invert: bool = None, all_points: bool = None) -> str:
    """
    Edit an existing data filter (threshold/extract selection).
    
    Args:
        name: The registered name of the filter to edit
        filter_type: Type of filter ("threshold" or "extract_selection")
        field_name: Name of the scalar field to filter by
        min_value: New minimum threshold value
        max_value: New maximum threshold value
        invert: New invert flag
        all_points: New all points flag (for threshold)
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the filter with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if filter_type is not None:
            filter_type = filter_type.lower()
            if filter_type in ["threshold", "extract_selection"]:
                # Filter type change may require recreation
                edited_props.append(f"filter type to {filter_type} (may require recreation)")
            else:
                return f"Unsupported filter type '{filter_type}'"
        
        if field_name is not None:
            if hasattr(proxy_to_edit, 'Scalars'):
                proxy_to_edit.Scalars = ['POINTS', field_name]
                edited_props.append(f"field name to {field_name}")
        
        if min_value is not None or max_value is not None:
            # Handle threshold range - use LowerThreshold/UpperThreshold for ParaView 5.10+ compatibility
            if min_value is not None:
                if hasattr(proxy_to_edit, 'LowerThreshold'):
                    proxy_to_edit.LowerThreshold = min_value
                    edited_props.append(f"minimum threshold to {min_value}")
            
            if max_value is not None:
                if hasattr(proxy_to_edit, 'UpperThreshold'):
                    proxy_to_edit.UpperThreshold = max_value
                    edited_props.append(f"maximum threshold to {max_value}")
        
        if invert is not None:
            if hasattr(proxy_to_edit, 'Invert'):
                proxy_to_edit.Invert = invert
                edited_props.append(f"invert to {invert}")
        
        if all_points is not None:
            # Note: AllPoints is not a valid property for Threshold filter in current ParaView version
            edited_props.append("all points (not directly editable in current ParaView version)")
        
        if edited_props:
            return f"Edited filter '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for filter '{name}'."
            
    except Exception as e:
        return f"Error editing filter: {str(e)}"

@mcp.tool()
def edit_calculated_field(name: str, result_name: str = None,
                          expression: str = None, attribute_mode: str = None) -> str:
    """
    Edit an existing calculated field (calculator).
    
    Args:
        name: The registered name of the calculator to edit
        result_name: New name for the calculated field
        expression: New mathematical expression to evaluate
        attribute_mode: New attribute mode ("Point Data" or "Cell Data")
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the calculator with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if result_name is not None:
            if hasattr(proxy_to_edit, 'ResultArrayName'):
                proxy_to_edit.ResultArrayName = result_name
                edited_props.append(f"result array name to {result_name}")
        
        if expression is not None:
            if hasattr(proxy_to_edit, 'Function'):
                proxy_to_edit.Function = expression
                edited_props.append(f"expression to '{expression}'")
        
        if attribute_mode is not None:
            attribute_mode = attribute_mode.strip()
            if attribute_mode in ["Point Data", "Cell Data"]:
                if hasattr(proxy_to_edit, 'AttributeType'):
                    proxy_to_edit.AttributeType = attribute_mode
                    edited_props.append(f"attribute mode to {attribute_mode}")
            else:
                return f"Attribute mode must be 'Point Data' or 'Cell Data', got '{attribute_mode}'"
        
        if edited_props:
            return f"Edited calculated field '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for calculated field '{name}'."
            
    except Exception as e:
        return f"Error editing calculated field: {str(e)}"

@mcp.tool()
def edit_transform(name: str, operation: str = None,
                   translate_x: float = None, translate_y: float = None, translate_z: float = None,
                   rotate_x: float = None, rotate_y: float = None, rotate_z: float = None,
                   scale_x: float = None, scale_y: float = None, scale_z: float = None) -> str:
    """
    Edit an existing geometric transform.
    
    Args:
        name: The registered name of the transform to edit
        operation: Transform type ("translate", "rotate", "scale", or "combined")
        translate_x, translate_y, translate_z: New translation amounts
        rotate_x, rotate_y, rotate_z: New rotation angles in degrees
        scale_x, scale_y, scale_z: New scale factors
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the transform with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if operation is not None:
            operation = operation.lower()
            if operation in ["translate", "rotate", "scale", "combined"]:
                # Operation type change may require recreation
                edited_props.append(f"operation to {operation} (may require recreation)")
            else:
                return f"Unsupported operation '{operation}'"
        
        # Translation
        if translate_x is not None or translate_y is not None or translate_z is not None:
            translation = []
            if translate_x is not None:
                translation.append(translate_x)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Translate'):
                    translation.append(proxy_to_edit.Transform.Translate[0])
                else:
                    translation.append(0.0)
            
            if translate_y is not None:
                translation.append(translate_y)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Translate'):
                    translation.append(proxy_to_edit.Transform.Translate[1])
                else:
                    translation.append(0.0)
                    
            if translate_z is not None:
                translation.append(translate_z)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Translate'):
                    translation.append(proxy_to_edit.Transform.Translate[2])
                else:
                    translation.append(0.0)
            
            if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Translate'):
                proxy_to_edit.Transform.Translate = translation
                edited_props.append(f"translation to {translation}")
        
        # Rotation
        if rotate_x is not None or rotate_y is not None or rotate_z is not None:
            rotation = []
            if rotate_x is not None:
                rotation.append(rotate_x)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Rotate'):
                    rotation.append(proxy_to_edit.Transform.Rotate[0])
                else:
                    rotation.append(0.0)
            
            if rotate_y is not None:
                rotation.append(rotate_y)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Rotate'):
                    rotation.append(proxy_to_edit.Transform.Rotate[1])
                else:
                    rotation.append(0.0)
                    
            if rotate_z is not None:
                rotation.append(rotate_z)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Rotate'):
                    rotation.append(proxy_to_edit.Transform.Rotate[2])
                else:
                    rotation.append(0.0)
            
            if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Rotate'):
                proxy_to_edit.Transform.Rotate = rotation
                edited_props.append(f"rotation to {rotation}")
        
        # Scaling
        if scale_x is not None or scale_y is not None or scale_z is not None:
            scale = []
            if scale_x is not None:
                scale.append(scale_x)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Scale'):
                    scale.append(proxy_to_edit.Transform.Scale[0])
                else:
                    scale.append(1.0)
            
            if scale_y is not None:
                scale.append(scale_y)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Scale'):
                    scale.append(proxy_to_edit.Transform.Scale[1])
                else:
                    scale.append(1.0)
                    
            if scale_z is not None:
                scale.append(scale_z)
            else:
                if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Scale'):
                    scale.append(proxy_to_edit.Transform.Scale[2])
                else:
                    scale.append(1.0)
            
            if hasattr(proxy_to_edit, 'Transform') and hasattr(proxy_to_edit.Transform, 'Scale'):
                proxy_to_edit.Transform.Scale = scale
                edited_props.append(f"scale to {scale}")
        
        if edited_props:
            return f"Edited transform '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for transform '{name}'."
            
    except Exception as e:
        return f"Error editing transform: {str(e)}"

@mcp.tool()
def edit_vector_visualization(name: str, glyph_type: str = None, vector_field: str = None,
                              scale_factor: float = None, scale_mode: str = None,
                              max_number_of_glyphs: int = None, auto_scale: bool = None,
                              scale_percentage: float = None) -> str:
    """
    Edit an existing vector field visualization (glyphs).
    
    Args:
        name: The registered name of the glyph filter to edit
        glyph_type: New glyph type ("arrow", "cone", "sphere", "line")
        vector_field: New vector field name
        scale_factor: New overall scaling factor for glyphs
        scale_mode: New scale mode ("vector", "scalar", or "off")
        max_number_of_glyphs: New maximum number of glyphs to display
        auto_scale: New auto-scale flag
        scale_percentage: New percentage of data diagonal for auto-scaling
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the glyph filter with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if glyph_type is not None:
            glyph_type = glyph_type.lower()
            glyph_type_map = {
                "arrow": "Arrow",
                "cone": "Cone",
                "sphere": "Sphere",
                "line": "Line"
            }
            glyph_type_name = glyph_type_map.get(glyph_type, "Arrow")
            if hasattr(proxy_to_edit, 'GlyphType'):
                proxy_to_edit.GlyphType = glyph_type_name
                edited_props.append(f"glyph type to {glyph_type}")
        
        if vector_field is not None:
            if hasattr(proxy_to_edit, 'OrientationArray'):
                proxy_to_edit.OrientationArray = ['POINTS', vector_field]
                edited_props.append(f"vector field to {vector_field}")
            if hasattr(proxy_to_edit, 'ScaleArray') and scale_mode != "off":
                proxy_to_edit.ScaleArray = ['POINTS', vector_field]
                edited_props.append(f"scale array to {vector_field}")
        
        if scale_factor is not None:
            if hasattr(proxy_to_edit, 'ScaleFactor'):
                proxy_to_edit.ScaleFactor = scale_factor
                edited_props.append(f"scale factor to {scale_factor}")
        
        if scale_mode is not None:
            scale_mode = scale_mode.lower()
            if scale_mode in ["vector", "scalar", "off"]:
                if scale_mode == "vector":
                    if hasattr(proxy_to_edit, 'VectorScaleMode'):
                        proxy_to_edit.VectorScaleMode = 'Scale by Magnitude'
                        edited_props.append(f"scale mode to vector")
                elif scale_mode == "scalar":
                    # ScaleArray already set appropriately above
                    if hasattr(proxy_to_edit, 'VectorScaleMode'):
                        proxy_to_edit.VectorScaleMode = 'Scale by Scalar'
                        edited_props.append(f"scale mode to scalar")
                else:  # off
                    if hasattr(proxy_to_edit, 'ScaleArray'):
                        proxy_to_edit.ScaleArray = ['POINTS', '']
                    if hasattr(proxy_to_edit, 'VectorScaleMode'):
                        proxy_to_edit.VectorScaleMode = 'Off'
                        edited_props.append(f"scale mode to off")
            else:
                return f"Scale mode must be 'vector', 'scalar', or 'off', got '{scale_mode}'"
        
        if max_number_of_glyphs is not None:
            if hasattr(proxy_to_edit, 'MaximumNumberOfSamplePoints'):
                proxy_to_edit.MaximumNumberOfSamplePoints = max_number_of_glyphs
                edited_props.append(f"maximum number of glyphs to {max_number_of_glyphs}")
        
        if auto_scale is not None:
            # Auto_scale affects how scale_factor is computed
            # This would require recomputing scale_factor based on data bounds
            edited_props.append(f"auto scale to {auto_scale} (scale factor may need recomputation)")
        
        if scale_percentage is not None:
            # Scale_percentage affects auto-computed scale factor
            edited_props.append(f"scale percentage to {scale_percentage} (scale factor may need recomputation)")
        
        if edited_props:
            return f"Edited vector visualization '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for vector visualization '{name}'."
            
    except Exception as e:
        return f"Error editing vector visualization: {str(e)}"

@mcp.tool()
def edit_field_analysis(name: str, analysis_type: str = None, field_name: str = None,
                        compute_vorticity: bool = None, compute_divergence: bool = None,
                        compute_qcriterion: bool = None) -> str:
    """
    Edit an existing field analysis (gradient/connectivity).
    
    Args:
        name: The registered name of the analysis filter to edit
        analysis_type: New analysis type ("gradient", "connectivity", or "combined")
        field_name: New field name to analyze
        compute_vorticity: New vorticity computation flag
        compute_divergence: New divergence computation flag
        compute_qcriterion: New Q-criterion computation flag
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the analysis filter with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if analysis_type is not None:
            analysis_type = analysis_type.lower()
            if analysis_type in ["gradient", "connectivity", "combined"]:
                # Analysis type change may require recreation
                edited_props.append(f"analysis type to {analysis_type} (may require recreation)")
            else:
                return f"Unsupported analysis type '{analysis_type}'"
        
        if field_name is not None:
            # For gradient analysis
            if hasattr(proxy_to_edit, 'ScalarArray'):
                proxy_to_edit.ScalarArray = ['POINTS', field_name]
                edited_props.append(f"field name to {field_name}")
        
        if compute_vorticity is not None:
            if hasattr(proxy_to_edit, 'ComputeVorticity'):
                proxy_to_edit.ComputeVorticity = compute_vorticity
                edited_props.append(f"compute vorticity to {compute_vorticity}")
        
        if compute_divergence is not None:
            if hasattr(proxy_to_edit, 'ComputeDivergence'):
                proxy_to_edit.ComputeDivergence = compute_divergence
                edited_props.append(f"compute divergence to {compute_divergence}")
        
        if compute_qcriterion is not None:
            if hasattr(proxy_to_edit, 'ComputeQCriterion'):
                proxy_to_edit.ComputeQCriterion = compute_qcriterion
                edited_props.append(f"compute Q-criterion to {compute_qcriterion}")
        
        if edited_props:
            return f"Edited field analysis '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for field analysis '{name}'."
            
    except Exception as e:
        return f"Error editing field analysis: {str(e)}"

@mcp.tool()
def edit_plot_over_line(name: str, point1: list[float] = None, point2: list[float] = None,
                        resolution: int = None) -> str:
    """
    Edit an existing plot over line filter.
    
    Args:
        name: The registered name of the plot over line filter to edit
        point1: New [x, y, z] coordinates of the start point
        point2: New [x, y, z] coordinates of the end point
        resolution: New number of sample points along the line
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the plot over line filter with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if point1 is not None:
            if len(point1) == 3:
                if hasattr(proxy_to_edit, 'Point1'):
                    proxy_to_edit.Point1 = point1
                    edited_props.append(f"point 1 to {point1}")
            else:
                return f"Point1 must be a list of 3 floats [x, y, z], got {point1}"
        
        if point2 is not None:
            if len(point2) == 3:
                if hasattr(proxy_to_edit, 'Point2'):
                    proxy_to_edit.Point2 = point2
                    edited_props.append(f"point 2 to {point2}")
            else:
                return f"Point2 must be a list of 3 floats [x, y, z], got {point2}"
        
        if resolution is not None:
            if resolution > 0:
                if hasattr(proxy_to_edit, 'Resolution'):
                    proxy_to_edit.Resolution = resolution
                    edited_props.append(f"resolution to {resolution}")
            else:
                return f"Resolution must be positive, got {resolution}"
        
        if edited_props:
            return f"Edited plot over line '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for plot over line '{name}'."
            
    except Exception as e:
        return f"Error editing plot over line: {str(e)}"

@mcp.tool()
def edit_warp_by_vector(name: str, vector_field: str = None,
                        scale_factor: float = None) -> str:
    """
    Edit an existing warp by vector filter.
    
    Args:
        name: The registered name of the warp by vector filter to edit
        vector_field: New vector field name to use for warping
        scale_factor: New scale factor for the warp
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the warp by vector filter with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if vector_field is not None:
            if hasattr(proxy_to_edit, 'Vectors'):
                proxy_to_edit.Vectors = ['POINTS', vector_field]
                edited_props.append(f"vector field to {vector_field}")
        
        if scale_factor is not None:
            if hasattr(proxy_to_edit, 'ScaleFactor'):
                proxy_to_edit.ScaleFactor = scale_factor
                edited_props.append(f"scale factor to {scale_factor}")
        
        if edited_props:
            return f"Edited warp by vector '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for warp by vector '{name}'."
            
    except Exception as e:
        return f"Error editing warp by vector: {str(e)}"

@mcp.tool()
def edit_delaunay3d(name: str, alpha: float = None, offset: float = None,
                    tolerance: float = None) -> str:
    """
    Edit an existing 3D Delaunay triangulation.
    
    Args:
        name: The registered name of the Delaunay3D filter to edit
        alpha: New alpha (distance) value
        offset: New offset multiplier for circumsphere radius
        tolerance: New tolerance for discarding degenerate tetrahedra
    
    Returns:
        Status message
    """
    try:
        from paraview.simple import GetSources, SetActiveSource
        
        sources_dict = GetSources()
        if not sources_dict:
            return "No sources available in the pipeline."
        
        # Find the Delaunay3D filter with the matching name
        proxy_to_edit = None
        for (key, proxy) in sources_dict.items():
            if key[0] == name:
                proxy_to_edit = proxy
                break
        
        if proxy_to_edit is None:
            return f"No source found with the name '{name}'."
        
        # Set as active source
        SetActiveSource(proxy_to_edit)
        
        # Edit properties
        edited_props = []
        
        if alpha is not None:
            if hasattr(proxy_to_edit, 'Alpha'):
                proxy_to_edit.Alpha = alpha
                edited_props.append(f"alpha to {alpha}")
        
        if offset is not None:
            if hasattr(proxy_to_edit, 'Offset'):
                proxy_to_edit.Offset = offset
                edited_props.append(f"offset to {offset}")
        
        if tolerance is not None:
            if hasattr(proxy_to_edit, 'Tolerance'):
                proxy_to_edit.Tolerance = tolerance
                edited_props.append(f"tolerance to {tolerance}")
        
        if edited_props:
            return f"Edited Delaunay3D '{name}': {', '.join(edited_props)}"
        else:
            return f"No properties edited for Delaunay3D '{name}'."
            
    except Exception as e:
        return f"Error editing Delaunay3D: {str(e)}"
