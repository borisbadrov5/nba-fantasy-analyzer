from app import db

class Player(db.Model):
	__tablename__ = "player"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	fg_pct_lvl = db.Column(db.String(100), nullable=False)
	ft_pct_lvl = db.Column(db.String(100), nullable=False)
	three_pm_pct_lvl = db.Column(db.String(100), nullable=False)
	reb_lvl = db.Column(db.String(100), nullable=False)
	ast_lvl = db.Column(db.String(100), nullable=False)
	stl_lvl = db.Column(db.String(100), nullable=False)
	blk_lvl = db.Column(db.String(100), nullable=False)
	pts_lvl = db.Column(db.String(100), nullable=False)
	to_lvl = db.Column(db.String(100), nullable=False)

	def __init__(self, id, name):
		self.id = id
		self.name = name