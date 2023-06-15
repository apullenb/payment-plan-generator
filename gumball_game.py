def play_game(box_ids, goals, num_jars, min_gumballs_list, gumballs_per_jar):
    num_boxes = len(box_ids)
    total_rounds = 0

    # Initialize the boxes with the minimum number of gumballs
    boxes = {box_id: min_gumballs for box_id, min_gumballs in zip(box_ids, min_gumballs_list)}

    # Game loop
    while not all(g <= boxes[box_id] for box_id, g in zip(box_ids, goals)):
        total_rounds += 1

        # Process each jar
        for jar in range(num_jars):
            # Distribute minimum gumballs to each box
            for box_id in box_ids:
                if boxes[box_id] < goals[box_ids.index(box_id)]:
                    diff = goals[box_ids.index(box_id)] - boxes[box_id]
                    gumballs_added = min(diff, boxes[box_id])
                    boxes[box_id] += gumballs_added
                    boxes[box_id] -= gumballs_added

            # If there are extra gumballs, allocate them to boxes based on goal priority
            for box_id in sorted(box_ids, key=lambda x: goals[box_ids.index(x)]):
                if min_gumballs <= 0:
                    break

                diff = goals[box_ids.index(box_id)] - boxes[box_id]
                gumballs_added = min(diff, min_gumballs)
                boxes[box_id] += gumballs_added
                min_gumballs -= gumballs_added

        # Record the state of boxes at the end of the round
        print(f"Round {total_rounds}")
        for jar in range(num_jars):
            print(f"Jar: {jar + 1}")
            for box_id in box_ids:
                print(f"Box {box_id}: {boxes[box_id]} gumballs")
            print()

        # Empty the boxes
        boxes = {box_id: 0 for box_id in box_ids}
        min_gumballs = gumballs_per_jar

    return total_rounds


# Get user input
box_ids = input("Enter the box IDs (comma-separated): ").split(",")
goals = list(map(int, input("Enter the goal numbers for each box (comma-separated): ").split(",")))
num_jars = int(input("Enter the number of jars: "))
min_gumballs_list = list(map(int, input("Enter the minimum number of gumballs for each box (comma-separated): ").split(",")))
gumballs_per_jar = int(input("Enter the number of gumballs per jar: "))

# Play the game
total_rounds = play_game(box_ids, goals, num_jars, min_gumballs_list, gumballs_per_jar)

# Print game summary
print("Game Over!")
print(f"Total Rounds: {total_rounds}")
