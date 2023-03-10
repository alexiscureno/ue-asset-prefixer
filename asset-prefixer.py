import unreal
import json

# Instance of Unreal Engine classes.
editor_util = unreal.EditorUtilityLibrary()
system_lib = unreal.SystemLibrary()


# Load the prefix mapping from a JSON file.
# This allows us to associate a class name with a prefix.
prefix_mapping = {}
with open("F:\\PycharmProjects\\UE\\ue-asset-prefixer\\prefix_mapping.json", 'r') as json_file:
    prefix_mapping = json.loads(json_file.read())

# Get the selected assets.
selected_assets = editor_util.get_selected_assets()
num_assets = len(selected_assets)
prefix = 0

# Loop through each selected asset.
for asset in selected_assets:
    # Get the asset's name and class.
    asset_name = system_lib.get_object_name(asset)
    asset_class = asset.get_class()
    class_name = system_lib.get_class_display_name(asset_class)

    # Get the prefix for the given class.
    class_prefix = prefix_mapping.get(class_name, None)

    if class_prefix is None:

        # If there is no prefix mapping for the class, log a warning and skip to the next asset.
        unreal.log_warning('No mapping for asset {} of type {}'.format(asset_name, class_name))
        continue
    if not asset_name.startswith(class_prefix):

        # If the asset's name doesn't already start with the prefix, rename it and add the prefix.
        new_name = class_prefix + asset_name
        editor_util.rename_asset(asset, new_name)
        prefix += 1
        unreal.log('Prefixed {} of type {} with {}'.format(asset_name, class_name, class_prefix))

    else:
        # If the asset's name already starts with the prefix, just log a message.
        unreal.log('Prefixed {} of {} assets.'.format(prefix, num_assets))

    # Log the name of the asset and its class.
    unreal.log('{} with class {} '.format(asset_name, class_name))