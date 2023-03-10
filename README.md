# UE Asset Prefixer

# ue-asset-prefixer

# Requirements 
* Unreal Engine 4.26 or later.
* Python 3.7 

# Installation

1. Clone the repository or download the zip file and extract its contents.
2. Copy and paste the script file and the json file into your Unreal Engine project's script folder.

# Usage

1. Select the assets you want to organize.
2. In the main menu, select File > Execute Python Script
3. Locate the script in your project's script folder and run it!.

# Notes
* The prefix_mapping.json file must be in the ue_asset_prefixer folder.
* The prefix is only added if the asset name does not already start with the prefix for that asset type.
* The script logs any warnings or errors encountered during the prefixing operation.
* This script does not create a backup of the original assets.
