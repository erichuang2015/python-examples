#!/usr/bin/env python3
# coding: utf-8

"""流畅的Python, Python风格的纸牌."""

import collections

from random import choice


# 定义一个具名元组
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


def main():
    deck = FrenchDeck()
    print(len(deck))
    # 支持索引
    print(deck[0], deck[-1])
    # 支持随机选取, 应该是调用了__getitem__方法
    print(choice(deck))
    # __getitem__方法支持切片, 因为直接传给self._cards
    print(deck[:3], deck[12::13])
    # 仅实现__getitem__方法, 就可迭代
    for card in deck:
        print(card)
    # 支持反向迭代
    for card in reversed(deck):
        print(card)
    # 支持 in 运算符
    print(Card('Q', 'hearts') in deck)
    print(Card('7', 'beasts') in deck)
    # 对deck排序
    for card in sorted(deck, key=spades_high):
        print(card)


if __name__ == '__main__':
    main()
