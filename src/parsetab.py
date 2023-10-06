
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AND BC BO CM COMMENT DIV DOUBLE DOUBLE_TYPE ELSE EQ ID IF INT INT_TYPE MAJ MAJ_EQ MIN MINUS MIN_EQ NEWLINE NOT OR PLUS PRINT RC RO S SC SO STAR WHILE WHITESPACEprog : decl_list stmt_listdecl_list : empty\n        | decl_list decl\n    empty :decl : type var_list Sstmt_list : stmt_list stmt\n        | stmt\n    stmt : IF\n        | WHILE\n        | assignment\n        | PRINT exp S\n        | BO stmt_list BC\n    assignment : id S\n        | id EQ exp S\n    type : INT_TYPE\n        | DOUBLE_TYPE\n    var_list : var\n        | var_list CM var\n    var : ID arrayarray : empty\n        | array SO INT SC\n    id : ID\n        | ID SO INT SC\n        | ID SO ID SC\n    exp : exp AND exp\n        | exp OR exp\n        | NOT exp\n        | exp EQ EQ exp\n        | exp MIN exp\n        | exp MAJ exp\n        | exp MAJ_EQ exp\n        | exp MIN_EQ exp\n        | exp PLUS exp\n        | exp MINUS exp\n        | exp STAR exp\n        | exp DIV exp\n        | RO exp RC\n        | id\n        | INT\n        | DOUBLE\n    '
    
_lr_action_items = {'IF':([0,2,3,4,5,6,8,9,10,12,17,27,28,31,35,49,67,],[-4,8,-2,8,-3,-7,-8,-9,-10,8,-6,8,-13,-5,-11,-12,-14,]),'WHILE':([0,2,3,4,5,6,8,9,10,12,17,27,28,31,35,49,67,],[-4,9,-2,9,-3,-7,-8,-9,-10,9,-6,9,-13,-5,-11,-12,-14,]),'PRINT':([0,2,3,4,5,6,8,9,10,12,17,27,28,31,35,49,67,],[-4,11,-2,11,-3,-7,-8,-9,-10,11,-6,11,-13,-5,-11,-12,-14,]),'BO':([0,2,3,4,5,6,8,9,10,12,17,27,28,31,35,49,67,],[-4,12,-2,12,-3,-7,-8,-9,-10,12,-6,12,-13,-5,-11,-12,-14,]),'INT_TYPE':([0,2,3,5,31,],[-4,13,-2,-3,-5,]),'DOUBLE_TYPE':([0,2,3,5,31,],[-4,14,-2,-3,-5,]),'ID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,17,22,23,27,28,29,30,31,32,35,36,37,39,40,41,42,43,44,45,46,49,57,67,],[-4,16,-2,16,-3,-7,20,-8,-9,-10,16,16,-15,-16,-6,16,16,16,-13,16,51,-5,20,-11,16,16,16,16,16,16,16,16,16,16,-12,16,-14,]),'$end':([1,4,6,8,9,10,17,28,35,49,67,],[0,-1,-7,-8,-9,-10,-6,-13,-11,-12,-14,]),'BC':([6,8,9,10,17,27,28,35,49,67,],[-7,-8,-9,-10,-6,49,-13,-11,-12,-14,]),'NOT':([11,22,23,29,36,37,39,40,41,42,43,44,45,46,57,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'RO':([11,22,23,29,36,37,39,40,41,42,43,44,45,46,57,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'INT':([11,22,23,29,30,36,37,39,40,41,42,43,44,45,46,54,57,],[25,25,25,25,52,25,25,25,25,25,25,25,25,25,25,70,25,]),'DOUBLE':([11,22,23,29,36,37,39,40,41,42,43,44,45,46,57,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'S':([15,16,18,19,20,21,24,25,26,33,34,47,50,53,55,56,58,59,60,61,62,63,64,65,66,68,69,71,72,],[28,-22,31,-17,-4,35,-38,-39,-40,-19,-20,-27,67,-18,-25,-26,-29,-30,-31,-32,-33,-34,-35,-36,-37,-24,-23,-28,-21,]),'EQ':([15,16,21,24,25,26,38,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[29,-22,38,-38,-39,-40,57,38,38,38,38,38,38,38,38,38,38,38,38,38,-37,-24,-23,38,]),'AND':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,36,-38,-39,-40,36,36,36,36,36,36,36,36,36,36,36,36,36,-37,-24,-23,36,]),'OR':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,37,-38,-39,-40,37,37,37,37,37,37,37,37,37,37,37,37,37,-37,-24,-23,37,]),'MIN':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,39,-38,-39,-40,39,39,39,39,39,39,39,39,39,39,39,39,39,-37,-24,-23,39,]),'MAJ':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,40,-38,-39,-40,40,40,40,40,40,40,40,40,40,40,40,40,40,-37,-24,-23,40,]),'MAJ_EQ':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,41,-38,-39,-40,41,41,41,41,41,41,41,41,41,41,41,41,41,-37,-24,-23,41,]),'MIN_EQ':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,42,-38,-39,-40,42,42,42,42,42,42,42,42,42,42,42,42,42,-37,-24,-23,42,]),'PLUS':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,43,-38,-39,-40,43,43,43,43,43,43,43,43,43,43,43,43,43,-37,-24,-23,43,]),'MINUS':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,44,-38,-39,-40,44,44,44,44,44,44,44,44,44,44,44,44,44,-37,-24,-23,44,]),'STAR':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,45,-38,-39,-40,45,45,45,45,45,45,45,45,45,45,45,45,45,-37,-24,-23,45,]),'DIV':([16,21,24,25,26,47,48,50,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,46,-38,-39,-40,46,46,46,46,46,46,46,46,46,46,46,46,46,-37,-24,-23,46,]),'RC':([16,24,25,26,47,48,55,56,58,59,60,61,62,63,64,65,66,68,69,71,],[-22,-38,-39,-40,-27,66,-25,-26,-29,-30,-31,-32,-33,-34,-35,-36,-37,-24,-23,-28,]),'SO':([16,20,33,34,72,],[30,-4,54,-20,-21,]),'CM':([18,19,20,33,34,53,72,],[32,-17,-4,-19,-20,-18,-21,]),'SC':([51,52,70,],[68,69,72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'prog':([0,],[1,]),'decl_list':([0,],[2,]),'empty':([0,20,],[3,34,]),'stmt_list':([2,12,],[4,27,]),'decl':([2,],[5,]),'stmt':([2,4,12,27,],[6,17,6,17,]),'type':([2,],[7,]),'assignment':([2,4,12,27,],[10,10,10,10,]),'id':([2,4,11,12,22,23,27,29,36,37,39,40,41,42,43,44,45,46,57,],[15,15,24,15,24,24,15,24,24,24,24,24,24,24,24,24,24,24,24,]),'var_list':([7,],[18,]),'var':([7,32,],[19,53,]),'exp':([11,22,23,29,36,37,39,40,41,42,43,44,45,46,57,],[21,47,48,50,55,56,58,59,60,61,62,63,64,65,71,]),'array':([20,],[33,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> prog","S'",1,None,None,None),
  ('prog -> decl_list stmt_list','prog',2,'p_prog','Lexical-Asignacion.py',155),
  ('decl_list -> empty','decl_list',1,'p_decl_list','Lexical-Asignacion.py',159),
  ('decl_list -> decl_list decl','decl_list',2,'p_decl_list','Lexical-Asignacion.py',160),
  ('empty -> <empty>','empty',0,'p_empty','Lexical-Asignacion.py',165),
  ('decl -> type var_list S','decl',3,'p_decl','Lexical-Asignacion.py',169),
  ('stmt_list -> stmt_list stmt','stmt_list',2,'p_stmt_list','Lexical-Asignacion.py',173),
  ('stmt_list -> stmt','stmt_list',1,'p_stmt_list','Lexical-Asignacion.py',174),
  ('stmt -> IF','stmt',1,'p_stmt','Lexical-Asignacion.py',179),
  ('stmt -> WHILE','stmt',1,'p_stmt','Lexical-Asignacion.py',180),
  ('stmt -> assignment','stmt',1,'p_stmt','Lexical-Asignacion.py',181),
  ('stmt -> PRINT exp S','stmt',3,'p_stmt','Lexical-Asignacion.py',182),
  ('stmt -> BO stmt_list BC','stmt',3,'p_stmt','Lexical-Asignacion.py',183),
  ('assignment -> id S','assignment',2,'p_assignment','Lexical-Asignacion.py',188),
  ('assignment -> id EQ exp S','assignment',4,'p_assignment','Lexical-Asignacion.py',189),
  ('type -> INT_TYPE','type',1,'p_type','Lexical-Asignacion.py',194),
  ('type -> DOUBLE_TYPE','type',1,'p_type','Lexical-Asignacion.py',195),
  ('var_list -> var','var_list',1,'p_var_list','Lexical-Asignacion.py',200),
  ('var_list -> var_list CM var','var_list',3,'p_var_list','Lexical-Asignacion.py',201),
  ('var -> ID array','var',2,'p_var','Lexical-Asignacion.py',206),
  ('array -> empty','array',1,'p_array','Lexical-Asignacion.py',210),
  ('array -> array SO INT SC','array',4,'p_array','Lexical-Asignacion.py',211),
  ('id -> ID','id',1,'p_id','Lexical-Asignacion.py',216),
  ('id -> ID SO INT SC','id',4,'p_id','Lexical-Asignacion.py',217),
  ('id -> ID SO ID SC','id',4,'p_id','Lexical-Asignacion.py',218),
  ('exp -> exp AND exp','exp',3,'p_exp','Lexical-Asignacion.py',223),
  ('exp -> exp OR exp','exp',3,'p_exp','Lexical-Asignacion.py',224),
  ('exp -> NOT exp','exp',2,'p_exp','Lexical-Asignacion.py',225),
  ('exp -> exp EQ EQ exp','exp',4,'p_exp','Lexical-Asignacion.py',226),
  ('exp -> exp MIN exp','exp',3,'p_exp','Lexical-Asignacion.py',227),
  ('exp -> exp MAJ exp','exp',3,'p_exp','Lexical-Asignacion.py',228),
  ('exp -> exp MAJ_EQ exp','exp',3,'p_exp','Lexical-Asignacion.py',229),
  ('exp -> exp MIN_EQ exp','exp',3,'p_exp','Lexical-Asignacion.py',230),
  ('exp -> exp PLUS exp','exp',3,'p_exp','Lexical-Asignacion.py',231),
  ('exp -> exp MINUS exp','exp',3,'p_exp','Lexical-Asignacion.py',232),
  ('exp -> exp STAR exp','exp',3,'p_exp','Lexical-Asignacion.py',233),
  ('exp -> exp DIV exp','exp',3,'p_exp','Lexical-Asignacion.py',234),
  ('exp -> RO exp RC','exp',3,'p_exp','Lexical-Asignacion.py',235),
  ('exp -> id','exp',1,'p_exp','Lexical-Asignacion.py',236),
  ('exp -> INT','exp',1,'p_exp','Lexical-Asignacion.py',237),
  ('exp -> DOUBLE','exp',1,'p_exp','Lexical-Asignacion.py',238),
]
