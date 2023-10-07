# Tic-Tac-Toe-MCTS
人工智能实验，通过蒙特卡洛树搜索实现井字棋的人机对弈。  
v1.0操作说明  
这是测试版，main还没有写。直接在`ttt-game.py`运行。  
参数`robot`表示是否启用机器人，参数`goes_first`表示启用机器人的时候是否先手。  
迭代次数和常量c暂时在`player.py`修改。在`make_a_move`方法中可以看到调用`MCTS`类，直接改就行。  
