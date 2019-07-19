import sys

import gym
import numpy as np
import gym.spaces
import random


class MyEnv(gym.Env):
    metadata = {'render.modes': ['human', 'ansi']}

    def __init__(self, racemat, labels, returns, pocket_money):
        super().__init__()
        self.racemat = racemat
        self.labels = labels
        self.returns = returns
        self.pocket_money = pocket_money

        # action_space, observation_space, reward_range を設定する
        self.action_space = gym.spaces.Discrete(
            len(self.labels[0]))  # 馬券の買い目全て
        self.observation_space = gym.spaces.Box(
            low=-20,
            high=20,
            shape=self.racemat[0].shape
        )
        self.reward_range = [-100., 7000000.]
        self.reset()

    def reset(self):
        # 諸々の変数を初期化する
        self.p_race = 0  # 現在のレース番号
        self.money = self.pocket_money  # スタートの所持金
        self.num_race = len(self.racemat)
        self.MAX_STEP = self.num_race
        self.p_label = self.labels[self.p_race]  # 今回のレースの勝ち馬券
        self.p_ret = self.returns[self.p_race]  # 今回のレースの払戻金
        self.done = False
        self.steps = 0
        return self.observe()

    def step(self, action):
        # 1ステップ進める処理を記述。戻り値は observation, reward, done(ゲーム終了したか),
        # info(追加の情報の辞書)

        # 馬券購入→払戻処理
        self.money -= 100
        reward = -100
        win_ticket = np.argmax(self.p_label)
        if action == win_ticket:
            reward += self.p_ret
            self.money += self.p_ret

        # 次のレースへ向けた処理
#        self.p_race += 1
        self.p_race = random.randrange(self.num_race)
        self.p_label = self.labels[self.p_race]
        self.p_ret = self.returns[self.p_race]
        # 次のレースの入力画像（出馬表）
        next_ob = self.observe()
        self.done = self.is_done()

        return next_ob, reward, self.done, {}

    def render(self, mode='human', close=False):
        # human の場合はコンソールに出力。ansiの場合は StringIO を返す
        outfile = StringIO() if mode == 'ansi' else sys.stdout
        message = str(self.money) + '\n'
        outfile.write(message)
        return outfile

    def close(self):
        pass

    def seed(self, seed=None):
        pass

    def observe(self):
        # レースの出馬表を返す
        observation = self.racemat[self.p_race]
        return observation

    def is_done(self):
        # 今回は最大で self.MAX_STEPS までとした
        if (self.money >= self.pockey_money * 10 or self.money < 0):
            return True
        elif self.steps > self.MAX_STEPS:
            return True
        else:
            return False
