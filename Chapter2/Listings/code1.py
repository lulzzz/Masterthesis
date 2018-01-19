'Choose maximum q value action and validate it'
    def choose_action_maxq(self, S):
        # choose an action according to the max q value
        action_names = []
        S = S.observation
        S_np = np.array(S)
        S = S_np[np.newaxis, :]
        action_values = self.sess.run(self.q_eval, feed_dict={self.s: S})
        for i in range(len(self.ACTIONS_INDEX)):
            temp = self.ACTIONS_INDEX[i][0]
            temp2 = action_values[0][temp]
            action_names.append([self.ACTIONS_INDEX[i][0], self.ACTIONS_INDEX[i][1], temp2])
        action_names.sort(key=self.getListKey, reverse=True)
        # check if the actions is valid, if not choose the next best one
        for j in range(len(action_names)):
            action = action_names[j][1]
            action_id = action_names[j][0]
            valid_action, out_of_stock = self.validate_action(action)
            if(valid_action == True): 
                break
        return action_id