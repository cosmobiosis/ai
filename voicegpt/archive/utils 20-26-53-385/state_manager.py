from transitions import Machine
from utils.state_manager_config import StateManagerConfig
import random

class StateManager(object):
    def __init__(self, config: StateManagerConfig):
        INITIAL_STATE = config.initial_state
        STATES = config.states
        TRANSITION_CONFIGS = config.transition_configs

        self.STATES = STATES

        # Initialize the state machine
        self.machine = Machine(model=self, states=STATES, initial=INITIAL_STATE)

        for transition_config in TRANSITION_CONFIGS:
            self.machine.add_transition(
                trigger=transition_config.name,
                source=transition_config.source_state.name, 
                dest=transition_config.destination_state.name
            )

