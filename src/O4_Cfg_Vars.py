""""Ortho4XP configuration variables."""

import O4_OSM_Utils as OSM


global_prefix = "global_"

cfg_app_vars = {
    # App
    "verbosity": {
        "module": "UI",
        "type": int,
        "default": 1,
        "values": (0, 1, 2, 3),
        "hint": "Verbosity determines the amount of information about the whole process which is printed on screen.  Critical errors, if any, are reported in all states as well as in the Log. Values above 1 are probably only useful for for debug purposes.",
    },
    "cleaning_level": {
        "module": "UI",
        "type": int,
        "default": 1,
        "values": (0, 1, 2, 3),
        "hint": "Determines which temporary files are removed. Level 3 erases everything except the config and what is needed for X-Plane; Level 2 erases everything except what is needed to redo the current step only; Level 1 allows you to redo any prior step; Level 0 keeps every single file.",
    },
    "overpass_server_choice": {
        "module": "OSM",
        "type": str,
        "default": "random",
        "values": ["random"] + sorted(OSM.overpass_servers.keys()),
        "hint": "The (country) of the Overpass OSM server used to grab vector data. It can be modified on the fly (as all _Application_ variables) in case of problem with a particular server.",
    },
    "skip_downloads": {
        "module": "TILE",
        "type": bool,
        "default": False,
        "hint": "Will only build the DSF and TER files but not the textures (neither download nor convert). This could be useful in cases where imagery cannot be shared.",
    },
    "skip_converts": {
        "module": "TILE",
        "type": bool,
        "default": False,
        "hint": "Imagery will be downloaded but not converted from jpg to dds. Some user prefer to postprocess imagery with third party softwares prior to the dds conversion. In that case Step 3 needs to be run a second time after the retouch work.",
    },
    "max_convert_slots": {
        "module": "TILE",
        "type": int,
        "default": 4,
        "values": (1, 2, 4, 6, 8, 12, 16, 24, 32, 64),
        "hint": "Number of parallel threads for dds conversion. Should be mainly dictated by the number of cores in your CPU.",
    },
    "check_tms_response": {
        "module": "IMG",
        "type": bool,
        "default": True,
        "hint": "When set, internal server errors (HTTP [500] and the likes) yields new requests, if not a white texture is used in place.",
    },
    "http_timeout": {
        "module": "IMG",
        "type": float,
        "default": 10.0,
        "hint": "Delay before we decide that a http request is timed out.",
    },
    "max_connect_retries": {
        "module": "IMG",
        "type": int,
        "default": 5,
        "hint": "How much times do we try again after a failed connection for imagery request. Only used if check_tms_response is set to True.",
    },
    "max_baddata_retries": {
        "module": "IMG",
        "type": int,
        "default": 5,
        "hint": "How much times do we try again after an internal server error for an imagery request. Only used if check_tms_response is set to True.",
    },
    "ovl_exclude_pol": {
        "module": "OVL",
        "type": list,
        "default": [0],
        "hint": 'Indices of polygon types which one would like to left aside in the extraction of overlays. The list of these indices in front of their name can be obtained by running the "extract overlay" process with verbosity = 2 (skip facades that can be numerous) or 3. Index 0 corresponds to beaches in Global and HD sceneries. Strings can be used in places of indices, in that case any polygon_def that contains that string is excluded, and the string can begin with a ! to invert the matching. As an exmaple, ["!.for"] would exclude everything but forests.',
    },
    "ovl_exclude_net": {
        "module": "OVL",
        "type": list,
        "default": [],
        "hint": "Indices of road types which one would like to left aside in the extraction of overlays. The list of these indices is can be in the roads.net file within X-Plane Resources, but some sceneries use their own corresponding net definition file. Powerlines have index 22001 in XP11 roads.net default file.",
    },
    "custom_scenery_dir": {
        "type": str,
        "default": "",
        "hint": 'Your X-Plane Custom Scenery. Used only for "1-click" creation (or deletion) of symbolic links from Ortho4XP tiles to there.',
    },
    "custom_overlay_src": {
        "module": "OVL",
        "type": str,
        "default": "",
        "hint": "The directory containing the sceneries with the overlays you would like to extract. You need to select the level of directory just _ABOVE_ Earth nav data.",
    },
    "custom_overlay_src_alternate": {
        "module": "OVL",
        "type": str,
        "default": "",
        "hint": "If sceneries with overlays are not found in custom_overlay_src, set an alternate directory to search.",
    },
}

cfg_tile_vars = {
    # Vector
    "apt_smoothing_pix": {
        "type": int,
        "default": 8,
        "hint": "How much gaussian blur is applied to the elevation raster for the look up of altitude over airports. Unit is the evelation raster pixel size.",
    },
    "road_level": {
        "type": int,
        "default": 1,
        "values": (0, 1, 2, 3, 4, 5),
        "hint": 'Allows to level the mesh along roads and railways. Zero means nothing such is included; "1" looks for banking ways among motorways, primary and secondary roads and railway tracks; "2" adds tertiary roads; "3" brings residential and unclassified roads; "4" takes service roads, and 5 finishes with tracks. Purge the small_roads.osm cached data if you change your mind in between the levels 2-5.',
    },
    "road_banking_limit": {
        "type": float,
        "default": 0.5,
        "hint": "How much sloped does a roads need to be to be in order to be included in the mesh levelling process. The value is in meters, measuring the height difference between a point in the center of a road node and its closest point on the side of the road.",
    },
    "lane_width": {
        "type": float,
        "default": 4.0,
        "hint": "Width (in meters) to be used for buffering that part of the road network that requires leveling.",
    },
    "max_levelled_segs": {
        "type": int,
        "default": 200000,
        "hint": "This limits the total number of roads segments included for mesh levelling, in order to keep triangle count under control in case of abundant OSM data.",
    },
    "water_simplification": {
        "type": float,
        "default": 0.0,
        "hint": "In case the OSM data for water areas would become too large, this parameter (in meter) can be used for node simplification.",
    },
    "min_area": {
        "type": float,
        "default": 0.001,
        "hint": "Minimum area (in km^2) a water patch needs to be in order to be included in the mesh as such. Contiguous water patches are merged before area computation.",
    },
    "max_area": {
        "type": float,
        "default": 200.0,
        "hint": "Any water patch larger than this quantity (in km^2) will be masked like the sea.",
    },
    "clean_bad_geometries": {
        "type": bool,
        "default": True,
        "hint": "When set, all OSM geometries are checked for self-intersection and merged between themselves in case of overlapping, allowing (hopefully!) to go around most OSM errors. This is computationally expensive, especially in places where OSM road/water data is detailed, and this is the reason for this switch, but if you are not in a hurry it is probably wise leaving it always activated.",
    },
    "mesh_zl": {
        "type": int,
        "default": 19,
        "values": (16, 17, 18, 19, 20),
        "hint": "The mesh will be preprocessed to accept later any combination of imageries up to and including a zoomlevel equal to mesh_zl. Lower value could save a few tens of thousands triangles, but put a limitation on the maximum allowed imagery zoomlevel.",
    },
    # Mesh
    "curvature_tol": {
        "type": float,
        "default": 2.0,
        "hint": "This parameter is intrinsically linked the mesh final density. Mesh refinement is mostly based on curvature computations on the elevation data (the exact decision rule can be found in _ triunsuitable() _ in Utils/Triangle4XP.c). A higher curvature tolerance yields fewer triangles.",
    },
    "apt_curv_tol": {
        "type": float,
        "default": 0.5,
        "hint": "If smaller, it supersedes curvature_tol over airports neighbourhoods.",
    },
    "apt_curv_ext": {
        "type": float,
        "default": 0.5,
        "hint": "Extent (in km) around the airports where apt_curv_tol applies.",
    },
    "coast_curv_tol": {
        "type": float,
        "default": 1.0,
        "hint": "If smaller, it supersedes curvature_tol along the coastline.",
    },
    "coast_curv_ext": {
        "type": float,
        "default": 0.5,
        "hint": "Extent (in km) around the coastline where coast_curv_tol applies.",
    },
    "limit_tris": {
        "type": float,
        "default": 3.0,
        "hint": "If non zero, approx upper bound _in millions_ on the number of final triangles in the mesh. Note: When 0 we impose a hard limit of 5M, to keep X-Plane comfortable. For high resolution DEMS you _should_ use it.",
    },
    "min_angle": {
        "type": float,
        "default": 10.0,
        "hint": "The mesh algorithm will try to not have mesh triangles with (smallest for water / second smallest for regular land) angle less than the value (in deg) of min_angle.",
    },
    "sea_smoothing_mode": {
        "type": str,
        "default": "zero",
        "values": ["zero", "mean", "none"],
        "hint": "Zero means that all nodes of sea triangles are set to zero elevation. With mean, some kind of smoothing occurs (triangles are levelled one at a time to their mean elevation), None (a value mostly appropriate for DEM resolution of 10m and less), positive altitudes of sea nodes are kept intact, only negative ones are brought back to zero, this avoids to create unrealistic vertical cliffs if the coastline vector data was lower res.",
    },
    "water_smoothing": {
        "type": int,
        "default": 10,
        "hint": "Number of smoothing passes over all inland water triangles (sequentially set to their mean elevation).",
    },
    "iterate": {
        "type": int,
        "default": 0,
        "hint": "Allows to refine a mesh using higher resolution elevation data of local scope only (requires Gdal), typically LIDAR data. Having an iterate number is handy to go backward one step when some choice of parameters needs to be revised. REQUIRES cleaning_level=0.",
    },
    # Masks
    "mask_zl": {
        "type": int,
        "default": 14,
        "values": (14, 15, 16),
        "hint": "The zoomlevel at which the (sea) water masks are built. Masks are used for alpha channel, and this channel usually requires less resolution than the RGB ones, the reason for this (VRAM saving) parameter. If the coastline and elevation data are very detailed, it might be interesting to lift this parameter up so that the masks can reproduce this complexity.",
    },
    "masks_width": {
        "type": list,
        "default": 100,
        "hint": "Maximum extent of the masks perpendicularly to the coastline (rough definition). NOTE: The value is now in meters, it used to be in ZL14 pixel size in earlier verions, the scale is roughly one to ten between both.",
    },
    "masking_mode": {
        "type": str,
        "default": "sand",
        "values": ["sand", "rocks", "3steps"],
        "hint": 'A selection of three tentative masking algorithms (still looking for the Holy Grail...). The first two (sand and rocks) requires masks_width to be a single value; the third one (3steps) requires a list of the form [a,b,c] for masks width: "a" is the length in meters of a first transition from plain imagery at the shoreline towards ratio_water transparency, "b" is the second extent zone where transparency level is kept constant equal to ratio_water, and "c" is the last extent where the masks eventually fade to nothing. The transition with rocks is more abrupt than with sand.',
    },
    "use_masks_for_inland": {
        "type": bool,
        "default": False,
        "hint": "Will use masks for the inland water (lakes, rivers, etc) too, instead of the default constant transparency level determined by ratio_water. This is VRAM expensive and presumably not really worth the price.",
    },
    "imprint_masks_to_dds": {
        "type": bool,
        "default": True,
        "hint": "Will apply masking directly to dds textures (at the Build Imagery/DSF step) rather than using external png files. This doubles the file size of masked textures (dxt5 vs dxt1) but reduce the overall VRAM footprint (a matter of choice!)",
    },
    "distance_masks_too": {
        "type": bool,
        "default": False,
        "hint": "This will additionally build distance to coastline masks that are used in Step 3 in order to improve the bathymetric profile (otherwise too low res) and avoid steep walls close to piers or rocks. Masks_zl should not be too low to grab these details.",
    },
    "masks_use_DEM_too": {
        "type": bool,
        "default": False,
        "hint": "If you have acces to high resolutions DEMs (really shines with 5m or lower), you can use the elevation in addition to the vector data in order to draw masks with higher precision. If the DEM is not high res, this option will yield unpleasant pixellisation.",
    },
    "masks_custom_extent": {
        "type": str,
        "default": "",
        "hint": 'Yet another tentative to draw masks with maximizing the use of the good imagery part. Requires to draw (JOSM) the "good imagery" threshold first, but it could be one order of magnitude faster to do compared to hand tweaking the masks and the imageries one by one.',
    },
    # DSF/Imagery
    "default_website": {"type": str, "default": "", "hint": ""},
    "default_zl": {"type": int, "default": 16, "hint": ""},
    "zone_list": {"type": list, "default": [], "hint": ""},
    "cover_airports_with_highres": {
        "type": str,
        "default": "False",
        "values": ("False", "True", "ICAO", "Existing"),
        "hint": 'When set, textures above airports will be upgraded to a higher zoomlevel, the imagery being the same as the one they would otherwise receive. Can be limited to airports with an ICAO code for tiles with so many airports. Exceptional: use "Existing" to (try to) derive custom zl zones from the textures directory of an existing tile.',
        "short_name": "high_zl_airports",
    },
    "cover_extent": {
        "type": float,
        "default": 1.0,
        "hint": "The extent (in km) past the airport boundary taken into account for higher ZL. Note that for VRAM efficiency higher ZL textures are fully used on their whole extent as soon as part of them are needed.",
    },
    "cover_zl": {
        "type": int,
        "default": 18,
        "hint": "The zoomlevel with which to cover the airports zone when high_zl_airports is set. Note that if the cover_zl is lower than the zoomlevel which would otherwise be applied on a specific zone, the latter is used.",
    },
    "sea_texture_blur": {
        "type": float,
        "default": 0.0,
        "hint": 'For layers of type "mask" in combined providers imageries, determines the extent (in meters) of the blur radius applied. This allows to smoothen some sea imageries where the wave or reflection pattern was too much present.',
    },
    "water_tech": {
        "type": str,
        "default": "XP11 + bathy",
        "values": ("XP12", "XP11 + bathy"),
        "hint": "Water tech type. XP12 uses a new (partly in construction) rendering tech, XP11 + bathy uses a more traditionnal blend. Both allows for 3D water.",
    },
    # "add_low_res_sea_ovl": {
    #    "type": bool,
    #    "default": False,
    #    "hint": "Will add an extra texture layer over the sea (with constant alpha channel given by ratio_water as for inland water), based on a low resolution imagery with global coverage. Masks with their full resolution imagery are still being used when present, the final render is a composite of both. The default imagery with code SEA can be changed as any other imagery defined in the Providers directory, it needs to have a max_zl defined and is used at its max_zl.",
    # },
    # "experimental_water": {
    #    "type": int,
    #    "default": 0,
    #    "values": (0, 1, 2, 3),
    #    "hint": 'If non zero, replaces X-Plane water by a custom normal map over low res ortho-imagery (requires XP11 but turns water rendering more XP10 alike). The value 0 corresponds to legacy X-Plane water, 1 replaces it for inland water only, 2 over sea water only, and 3 over both. Values 2 and 3 should always be used in combination with "imprint_masks_to_dds".\n\nThis experimental feature has two strong downsides: 1) the waves are static rather dynamical (would require a plugin to update the normal_map as X-Plane does) and 2) the wave height is no longer weather dependent. On the other hand, waves might have less repetitive patterns and some blinking in water reflections might be improved too; users are welcome to improve the provided water_normal_map.dds (Gimp can be used to edit the mipmaps individually).',
    # },
    "ratio_water": {
        "type": float,
        "default": 0.25,
        "hint": 'Inland water rendering is made of two layers : one bottom layer of "X-Plane water" and one overlay layer of orthophoto with constant level of transparency applied. The parameter ratio_water (values between 0 and 1) determines how much transparency is applied to the orthophoto. At zero, the orthophoto is fully opaque and X-Plane water cannot be seen ; at 1 the orthophoto is fully transparent and only the X-Plane water is seen.',
    },
    "ratio_bathy": {
        "type": float,
        "default": 1.0,
        "hint": "Bathymetry multiplier for near shore vertices. In the range [0,1].",
    },
    "normal_map_strength": {
        "type": float,
        "default": 1.0,
        "hint": 'Orthophotos by essence already contain the part of the shading burned in (here by shading we mean the amount of reflected light in the camera direction as a function of the terrain slope, not the shadows). This option allows to tweak the normal coordinates of the mesh in the DSF to avoid "overshading", but it has side effects on the way X-Plane computes scenery shadows. Used to be 0.3 by default in earlier versions, the default is now 1 which means exact normals.',
    },
    "terrain_casts_shadows": {
        "type": bool,
        "default": True,
        "hint": "If unset, the terrain itself will not cast (but still receive!) shadows. This option is only meaningful if scenery shadows are opted for in the X-Plane graphics settings.",
        "short_name": "terrain_casts_shadow",
    },
    "overlay_lod": {
        "type": float,
        "default": 25000,
        "hint": "Distance until which overlay imageries (that is orthophotos over water) are drawn. Lower distances have a positive impact on frame rate and VRAM usage, and IFR flyers will probably need a higher value than VFR ones.",
    },
    "use_decal_on_terrain": {
        "type": bool,
        "default": False,
        "hint": "Terrain files for all but water triangles will contain the maquify_1_green_key.dcl decal directive. The effect is noticeable at very low altitude and helps to overcome the orthophoto blur at such levels. Can be slightly distracting at higher altitude.",
    },
    # Other
    "custom_dem": {
        "type": str,
        "default": "",
        "hint": "Path to an elevation data file to be used instead of the default Viewfinderpanoramas.org ones (J. de Ferranti). The raster must be in geopgraphical coordinates (EPSG:4326) but the extent need not match the tile boundary (requires Gdal). Regions of the tile that are not covered by the raster are mapped to zero altitude (can be useful for high resolution data over islands in particular).",
    },
    "fill_nodata": {
        "type": bool,
        "default": True,
        "hint": "When set, the no_data values in the raster will be filled by a nearest neighbour algorithm. If unset, they are turned into zero (can be useful for rasters with no_data over the whole oceanic part or partial LIDAR data).",
    },
}

# Create dictionary from cfg_tile_vars with prefix and remove keys not in global config
cfg_global_tile_vars = {
    f"{global_prefix}{key}": value
    for key, value in cfg_tile_vars.items()
    if key not in ["default_website", "default_zl", "zone_list"]
}

cfg_vars = {**cfg_app_vars, **cfg_tile_vars, **cfg_global_tile_vars}

list_app_vars = [
    "verbosity",
    "cleaning_level",
    "overpass_server_choice",
    "skip_downloads",
    "skip_converts",
    "max_convert_slots",
    "check_tms_response",
    "http_timeout",
    "max_connect_retries",
    "max_baddata_retries",
    "ovl_exclude_pol",
    "ovl_exclude_net",
    "custom_scenery_dir",
    "custom_overlay_src",
    "custom_overlay_src_alternate",
]

gui_app_vars_short = list_app_vars[:-3]

gui_app_vars_long = list_app_vars[-3:]

list_vector_vars = [
    "apt_smoothing_pix",
    "road_level",
    "road_banking_limit",
    "lane_width",
    "max_levelled_segs",
    "water_simplification",
    "min_area",
    "max_area",
    "clean_bad_geometries",
    "mesh_zl",
]

list_mesh_vars = [
    "curvature_tol",
    "apt_curv_tol",
    "apt_curv_ext",
    "coast_curv_tol",
    "coast_curv_ext",
    "limit_tris",
    "min_angle",
    "sea_smoothing_mode",
    "water_smoothing",
    "iterate",
]

list_mask_vars = [
    "mask_zl",
    "masks_width",
    "masking_mode",
    "use_masks_for_inland",
    "imprint_masks_to_dds",
    "distance_masks_too",
    "masks_use_DEM_too",
    "masks_custom_extent",
]

list_dsf_vars = [
    "cover_airports_with_highres",
    "cover_extent",
    "cover_zl",
    "water_tech",
    "ratio_bathy",
    "ratio_water",
    "overlay_lod",
    "sea_texture_blur",
    # "add_low_res_sea_ovl",
    # "experimental_water",
    "normal_map_strength",
    "terrain_casts_shadows",
    "use_decal_on_terrain",
]

list_other_vars = ["custom_dem", "fill_nodata"]

list_tile_vars = (
    list_vector_vars
    + list_mesh_vars
    + list_mask_vars
    + list_dsf_vars
    + list_other_vars
    + ["default_website", "default_zl", "zone_list"]
)

list_global_tile_vars = [
    global_prefix + item
    for item in (
        list_vector_vars
        + list_mesh_vars
        + list_mask_vars
        + list_dsf_vars
        + list_other_vars
    )
]

list_global_vector_vars = [global_prefix + item for item in list_vector_vars]

list_global_mesh_vars = [global_prefix + item for item in list_mesh_vars]

list_global_dsf_vars = [global_prefix + item for item in list_dsf_vars]

list_global_mask_vars = [global_prefix + item for item in list_mask_vars]

list_cfg_vars = list_tile_vars + list_global_tile_vars + list_app_vars