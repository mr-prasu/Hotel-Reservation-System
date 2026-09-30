# Room Management System

A beginner-friendly, menu-driven hotel room management program written in Python. It demonstrates basic functions, lists, dictionaries, loops, input validation, and simple billing through a terminal interface.

## Features

- Display a fixed list of five rooms with room type, rate, and floor.
- Register a guest by entering a name, 10-digit phone number, and 12-character ID proof.
- Check guests into rooms and record a stay duration.
- Add breakfast, lunch, or dinner orders for occupied rooms.
- Print a bill and booking-history summary.
- Check a guest out and remove the room from the occupied-room list.

## Requirements

- Python 3.10 or newer is recommended. The source uses modern f-string syntax in billing/history output.
- No third-party packages are used.

## Run the program

Open a terminal in this folder and run:

```bash
python main.py
```

The menu lets you choose an action by number. Room choices during check-in are entered using the room's position in the displayed list (1–5), while later actions generally ask for the actual room number (101–105).

## Project files

- `main.py` prints the menu, reads the user's choice, calls the matching function, and returns to the menu.
- `room_management.py` contains the room data and the registration, check-in, food-ordering, billing, history, and check-out functions.

## How the code works

### Menu (`main.py`)

`main.py` imports the functions from `room_management.py`. The `function()` routine prints the options, validates that the selection is between 1 and 8, and calls the corresponding operation. It calls itself again after each operation so the menu appears again. Option 8 exits.

### Data and room list (`room_management.py`)

- `room_no` starts with the room numbers 101–105.
- `room` stores each room's type, price, and floor as strings.
- `l` holds registered guest dictionaries; each record contains a name, phone number, ID proof, and registration date.
- `cus_r` tracks occupied room numbers.
- `number_hr` maps an occupied room number to the entered stay duration.
- `breakfast`, `lunch`, and `dinner` are dictionaries mapping menu-item names to prices. `food_details` stores food totals by room.

These values are ordinary Python variables, so they are reset whenever the program exits. The program does not save data to a file or database.

### Main operations

- `rooms()` prints the room list.
- `registration()` validates guest details and adds a record to `l`.
- `check_in()` asks how many rooms to book, collects room choices and stay duration, and updates occupied-room data.
- `food_service()` selects a meal menu, accepts food and quantity, and records a food total for the room.
- `generate_bill()` and `view_booking_history()` display room, food, and fixed-charge information.
- `check_out()` removes the room from the occupied list and deletes its stay and food entries.

## Current limitations to be aware of

This is an early learning project, and some behaviors need improvement before the program can be relied on for real bookings:

- Guest registration is not connected to a room or check-in record.
- Check-in and room availability handling has inconsistent use of room-list positions and room numbers; selecting multiple rooms may not work correctly.
- The stay duration is entered in check-in, but it is not tied reliably to each selected room in all cases.
- Food selection checks only that the input contains letters, not that it is a valid item; an unknown item can cause a lookup error. Menu item names containing spaces are also rejected by that check.
- Food totals and bill totals use shared global variables, so totals can carry over between rooms or operations.
- Billing/history use the requested room count to find room pricing, rather than reliably looking up the chosen room. A bill with no food order may also hit an undefined food amount.
- Booking history is calculated from current in-memory values, not stored historical transactions.
- The menu repeats by calling itself recursively; a loop would be safer for long sessions.
- Rates and charges are hard-coded, and no payment is actually processed.

## Suggested two-day explanation plan

### Day 1: Structure and guest flow

1. Run through the menu and identify which function each option calls.
2. Study `room_no`, `room`, and the guest/occupancy data structures.
3. Trace `rooms()`, `registration()`, and `check_in()` with a sample booking.
4. Explain how input loops validate values and how global lists/dictionaries hold session state.

### Day 2: Services, billing, and improvements

1. Trace a food order through `food_service()` and its price dictionaries.
2. Follow how `generate_bill()` and `view_booking_history()` assemble totals.
3. Explain how `check_out()` removes occupancy data.
4. Identify the limitations above and outline improvements: use a menu loop, validate menu keys, keep data per room, look up room rates by room number, and save records persistently.

## Learning concepts shown

- Python functions and imports
- Lists, dictionaries, loops, and conditionals
- String and numeric input validation
- Global state and basic date handling
- Formatted terminal output
