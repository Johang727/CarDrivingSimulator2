## **v0.1.0-infdev - 20 May 2025**
**+7,888 Blocks; +24.2 MB**
- The start of a new era, Car Driving Simulator 2
- Debug Console added from another one of my games
- Engine built
    - Engine can be turned off and on (Rather than Park = Off)
    - Has multiple gears (unlike the single variable gear like CDS1)
    - Revs are calclated based on gear and speed
    - Reverse is like a Gear 1
    - Car health directly limits max throttle
    - Engines are not hardcoded and can be swapped out
- Dashboard built (v0)
- Car visual actually added
    - Same movement as previous game, apart from "dashing" by double-tapping the movement keys
- Other cars added
    - Limited to 10, but it's really simple to change
        - Limited to this so that a list of other car positions can be made
- Title Screen
    - Everything was built with one in mind
        - Allows you to switch starting transmission and quality
        - Basically all it has so far, however, more comes soon.
- Gas station has an interior
    - Also has a shop where you can buy phone
- Dialog Box added from another one of my games
    - Shows up in Gas Station + Dealership
- Challenges
    - Only speed challenge implemented, however 3 others are planned (with more to come!)
- Particle system added with global functions (messages)
    - Crash particles show when cars crash into each other
    - Smoke particles show when car health is <20%
    - Particles cover the numbers when shifting
        - Red: Late Shift
        - Yellow: Early Shift
        - Green: Good Shift
        - Cyan: Perfect Shift
- On-screen hint system added
    - It's a little buggy tho
- Ambient music added
    - Intended to change throughout the day, but for now I only have one
- Car dealership added
    - You can change engines here
    - Cannot buy cars yets
- Added FPS counter