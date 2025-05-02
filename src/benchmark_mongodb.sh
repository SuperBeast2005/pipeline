#!/bin/bash

SESSION="etl_session"

# Start new tmux session in detached mode
tmux new-session -d -s $SESSION

# Run producer.py in the first pane
tmux send-keys -t $SESSION "python3 producer.py" C-m

# Split window and run consumer.py in the second pane
tmux split-window -h -t $SESSION
tmux send-keys -t $SESSION "python3 consumer_mongo.py" C-m

# Attach to the tmux session
tmux attach-session -t $SESSION