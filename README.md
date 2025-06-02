# Blender Preset Saver Addon

This Blender addon enables saving and applying comprehensive presets for your objects, including:

- **Object Transforms** (location, rotation, scale)  
- **Modifiers** (all types on the object)  
- **Materials** (active material on the object with full shader node trees)  
- **Geometry Nodes Modifiers** (full node trees, nodes, connections, and custom values)  

## Features

- **Save complete object setup** into reusable Python scripts for later application.  
- Preserve all **customized values** in shader nodes (ColorRamp stops, input parameters), Geometry Nodes (node properties, socket values), modifiers, and transforms.  
- Reapply presets to multiple selected objects at once.  
- Automatically remove previous presets/modifiers to avoid duplicates or conflicts.  
- Support for complex node setups and modifier stacks.  
- Exported presets are easy to share and version-control as simple Python files.  

## Why Choose This Addon?

Compared to existing Blender presets and asset management tools, this addon offers:

- **Full scene object-level presets** — not just materials or modifiers individually, but a combined snapshot of transforms, modifiers, materials, and geometry nodes in one place.  
- **Preserves all custom node settings** including detailed ColorRamp stops and input socket defaults, which many existing addons ignore or partially support.  
- **Lightweight, script-based presets** instead of bulky binary files or Blender asset libraries, making integration with version control and automation easier.  
- **Simple workflow** — save your current state to a `.py` script, then apply it to any object(s) with a single script execution.  
- No need for external dependencies or complex asset management systems.

## How to Use

1. Select an object in Blender.  
2. Run the “Save Preset” operator to export a `.py` script preset capturing transforms, modifiers, materials, and geometry nodes.  
3. To apply, run the exported `.py` script in Blender with your target objects selected. The addon recreates the saved setup exactly.

Tutorial Link : https://youtu.be/65UdsYL98XY?si=9w6qNvk1-QYQsTEe

## Installation

- Download PreSave.zip from Releases.
- Copy the extracted zip file into Blender’s addons folder, or install via *Edit > Preferences > Add-ons > Install...*  
- Enable the addon in the preferences.  
- Access the save/apply preset operators through the search menu or custom UI.

---

*Simplify your workflow, save time, and keep your Blender objects perfectly consistent across scenes and projects!*
