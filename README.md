# FrameMaster
Custom Video Editing Hardware  
<img width="500" height="400" alt="image" src="https://github.com/user-attachments/assets/c1a7b21a-6955-454f-99e9-2a3355e6e0e4" />

## What It Is
A open source alternative to expensive video editing hardware. Intended to fall between inexpensive video editing jog wheels (like the $160 [TourBox NEO](https://www.amazon.com/Upgraded-TourBox-NEO-Controller-Customized/dp/B08HCV1JGB) )  and high-end hardware (like the $435 [Davinci Resolve Speed Editor](https://www.amazon.com/Blackmagic-Design-Davinci-Bluetooth-Activation/dp/B08QLN4ZZN/) )

<img width="643" height="493" alt="image" src="https://github.com/user-attachments/assets/ace7f080-72c0-4dcc-9f9d-becfb92b112b" />


## What Can It Do?
Out of the box it can:
- Use its jog wheel to advance through frames with both high speed and precision.
- Mark In and Mark Out when defining clips
- Perform both Standard Deletes and Ripple Deletes
- Instert Clips

## What Else can it do?
Because this is open source and you will be printing the key caps yourself, you can make it do literally anything. There is code provided that demonstrates how to have the FrameMaster send keyboard commands to your video editing software. Any command you want, just add it to the python script.

<img width="1155" height="888" alt="image" src="https://github.com/user-attachments/assets/cbeabdd7-65d5-4ac1-ac3b-70f1fd758aee" />


## What do I need to make it?
You will need:
- A circuit board manufacturing service. I used PCBway, but JLCPCB seems to be just as good.
- A raspberry Pi Pico with header pins and female mounting pins. If you are comfortable soldering the header pins yourself you can save a dollar and get a non-presoldered one. But it is designed to accommodate a pre-soldered Pico
- 9 MX switches. These are the standard switches that are found in mechanical keyboards.
- A rotary encoder.
- A 5 Pin 90 degree header and Dupont connectors to connect the rotary encoder to the main board. All other wiring is inside of the main board and does not need to be done by hand.
- Some small Metric socket cap screws and matching inserts. I used M2.5.
- A 3d printer. Almost any printer will work to make the case. To print the keycaps is a little more challenging, and if you are not familiar with printing with minimal bed contact it may be easier to just purchase some inexpensive keycaps.

<img width="835" height="613" alt="image" src="https://github.com/user-attachments/assets/17a5db38-46e3-4840-87ad-6f458f425002" />
