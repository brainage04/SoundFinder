# Instructions
You will need to clone this repository before completing any other instructions.

You will need to import the `objects` folder from your desired Minecraft version's `.jar` file. To do this, locate your `.minecraft` installation:

Windows: Win+R, type in `%appdata%` and click on `.minecraft`
Mac: I don't know (sorry)
Linux: In the current user directory (`/home/{username}/.minecraft`)

Navigate to `versions/{version}` and copy `{version}.json` and `{version}.jar` into this folder, then extract this file into a new folder (can be done with `Extract Here` on Windows/Linux or `7-Zip > Extract to '*/'` on supported operating systems)

Navigate to `assets/objects` and copy this folder to the top level (the same level as this README.md file is in). You can now delete the .jar/extracted folder and run the `main.py` script.

The script will prompt you to enter a string to match in the `{version}.json` file. You can match for groups of sounds (such as `villager`) or types of sounds across all groups (such as `death`).