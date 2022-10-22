import sys
import time
from constants import *
from environment import *
from state import State
"""
solution.py

This file is a template you should use to implement your solution.

You should implement code for each of the TODO sections below.

COMP3702 2022 Assignment 3 Support Code

Last updated by njc 12/10/22
"""

DEFAULT_NUM_EPS = 1000


def is_converged():
    return False

def q_funct():
    return 0

class RLAgent:

    #
    # TODO: (optional) Define any constants you require here.
    #

    def __init__(self, environment: Environment):
        self.environment = environment
        # TODO: (optional) Define any class instance variables you require (e.g. Q-value tables) here.

        # Get initial state
        self.current_state = environment.get_init_state()
        self.states = []
        self.states.append(self.current_state)

        # Create Q-value table
        self.q_values = dict()

        self.num_eps = DEFAULT_NUM_EPS                                      # num of episodes to run

    # === Q-learning ===================================================================================================

    def q_learn_train(self):
        """
        Train this RL agent via Q-Learning.
        """
        #
        # TODO: Implement your Q-learning training loop here.
        #

        for i in range(self.num_eps):

            if is_converged():
                break
            else:
                # select and perform action
                action = self.q_learn_select_action(self.current_state)
                reward, new_state = self.environment.perform_action(self.current_state, action)

                # calculate q-function
                q_val = q_funct()
                new_q_val = q_funct()
                if q_val in self.q_values.keys():
                    pass
                else:
                    self.q_values[]


    def q_learn_select_action(self, state: State):
        """
        Select an action to perform based on the values learned from training via Q-learning.
        :param state: the current state
        :return: approximately optimal action for the given state
        """
        #
        # TODO: Implement code to return an approximately optimal action for the given state (based on your learned
        #  Q-learning Q-values) here.
        #
        return 0

    # === SARSA ========================================================================================================

    def sarsa_train(self):
        """
        Train this RL agent via SARSA.
        """
        #
        # TODO: Implement your SARSA training loop here.
        #
        pass

    def sarsa_select_action(self, state: State):
        """
        Select an action to perform based on the values learned from training via SARSA.
        :param state: the current state
        :return: approximately optimal action for the given state
        """
        #
        # TODO: Implement code to return an approximately optimal action for the given state (based on your learned
        #  SARSA Q-values) here.
        #
        pass

    # === Helper Methods ===============================================================================================
    #
    #
    # TODO: (optional) Add any additional methods here.
    #
    #

