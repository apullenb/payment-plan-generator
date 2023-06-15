def play_game(box_ids, goals, num_jars, gumballs_per_jar):
    num_boxes = len(box_ids)
    total_rounds = 0

    # Initialize the boxes with the minimum number of gumballs
    boxes = {box_id: n for box_id, n in zip(box_ids, goals)}

    # Game loop
    while not all(g <= boxes[box_id] for box_id, g in zip(box_ids, goals)):
        total_rounds += 1
        gumballs_left = gumballs_per_jar

        # Distribute gumballs from the first jar
        for box_id in box_ids:
            diff = goals[box_ids.index(box_id)] - boxes[box_id]
            gumballs_added = min(diff, gumballs_left)
            boxes[box_id] += gumballs_added
            gumballs_left -= gumballs_added

            if gumballs_left == 0:
                break

        # If some boxes haven't reached their goals, record the state
        if not all(g <= boxes[box_id] for box_id, g in zip(box_ids, goals)):
            print(f"Round {total_rounds}")
            print(f"Jar: 1")
            for box_id in box_ids:
                print(f"Box {box_id}: {boxes[box_id]} gumballs")
            print()

        # Empty the boxes
        boxes = {box_id: 0 for box_id in box_ids}

        # Process the remaining jars
        for jar in range(1, num_jars):
            gumballs_left = gumballs_per_jar

            for box_id in box_ids:
                diff = goals[box_ids.index(box_id)] - boxes[box_id]
                gumballs_added = min(diff, gumballs_left)
                boxes[box_id] += gumballs_added
                gumballs_left -= gumballs_added

                if gumballs_left == 0:
                    break

            # If some boxes haven't reached their goals, record the state
            if not all(g <= boxes[box_id] for box_id, g in zip(box_ids, goals)):
                print(f"Round {total_rounds}")
                print(f"Jar: {jar+1}")
                for box_id in box_ids:
                    print(f"Box {box_id}: {boxes[box_id]} gumballs")
                print()

            # Empty the boxes
            boxes = {box_id: 0 for box_id in box_ids}

    return total_rounds


# Get user input
box_ids = input("Enter the box IDs (comma-separated): ").split(",")
goals = list(map(int, input("Enter the goal numbers for each box (comma-separated): ").split(",")))
num_jars = int(input("Enter the number of jars: "))
gumballs_per_jar = int(input("Enter the number of gumballs per jar: "))

# Play the game
total_rounds = play_game(box_ids, goals, num_jars, gumballs_per_jar)

# Print game summary
print("Game Over!")
print(f"Total Rounds: {total_rounds}")
