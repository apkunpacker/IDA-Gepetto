# Original Project
https://github.com/JusticeRage/Gepetto
# IDA-Gepetto
Gepetto is a Python script which uses Local LLM to provide meaning to functions decompiled by IDA Pro. At the moment, it can ask any local model to explain what a function does, and to automatically rename its variables. Here is a simple example of what results it can provide in mere seconds:

<img width="595" alt="IDA" src="https://github.com/apkunpacker/IDA-Gepetto/assets/27184655/565daaaf-7c39-401d-b411-17b2dd90aad3">

## Setup

Simply drop this script (as well as the `gepetto/` folder) into your IDA plugins folder (`$IDAUSR/plugins`). 
By default, on Windows, this should be `%AppData%\Hex-Rays\IDA Pro\plugins` (you may need to create the folder).

You will need to add the required packages to IDA's Python installation for the script to work.
Find which interpreter IDA is using by checking the following registry key: 
`Computer\HKEY_CURRENT_USER\Software\Hex-Rays\IDA` (default on Windows: `%LOCALAPPDATA%\Programs\Python\Python39`).

## Usage

Once the plugin is installed properly, you should be able to invoke it from the context menu of IDA's pseudocode window,
as shown in the screenshot below:
<img width="1410" alt="Use" src="https://github.com/apkunpacker/IDA-Gepetto/assets/27184655/f9d5d787-2ce7-4800-93e7-63ba7686a114">

You can also use the following hotkeys:

- Ask the model to explain the function: `Ctrl` + `Alt` + `H`
- Request better names for the function's variables: `Ctrl` + `Alt` + `R`

Initial testing shows that asking for better names works better if you ask for an explanation of the function first – I
assume because the model then uses its own comment to make more accurate suggestions.
There is an element of randomness to the AI's replies. If for some reason the initial response you get doesn't suit you,
you can always run the command again.

