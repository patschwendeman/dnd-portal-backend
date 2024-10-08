from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Table
from sqlalchemy.orm import relationship
from src.db.database import Base

# pylint: disable=too-few-public-methods

scene_music_association = Table(
    'scene_music_association', Base.metadata,
    Column('scene_id', Integer, ForeignKey('scene.id')),
    Column('music_id', Integer, ForeignKey('music.id'))
)

class GraphicsWall(Base):
    __tablename__ = 'graphics_wall'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    source = Column(String)
    scene = relationship("Scene", back_populates="graphics_wall", uselist=False)

class GraphicsGround(Base):
    __tablename__ = 'graphics_ground'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    source = Column(String)
    scene = relationship("Scene", back_populates="graphics_ground", uselist=False)

class Music(Base):
    __tablename__ = 'music'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    source = Column(String)
    scenes = relationship('Scene', secondary=scene_music_association, back_populates='music')

class BattleMap(Base):
    __tablename__ = 'battlemaps'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    loot = Column(String)
    xp = Column(String)
    enemies = Column(String)
    locked = Column(Boolean)
    source= Column(String)
    source_locked = Column(String)
    scene = relationship("Scene", back_populates="battlemaps", uselist=False)

class Scene(Base):
    __tablename__ = 'scene'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(Text)
    fight = Column(Boolean)
    graphics_wall_id = Column(Integer, ForeignKey('graphics_wall.id'))
    graphics_wall = relationship("GraphicsWall", back_populates="scene", uselist=False)
    graphics_ground_id = Column(Integer, ForeignKey('graphics_ground.id'), unique=True)
    graphics_ground = relationship("GraphicsGround", back_populates="scene", uselist=False)
    battlemaps_id = Column(Integer, ForeignKey('battlemaps.id'), unique=True)
    battlemaps = relationship("BattleMap", back_populates="scene", uselist=False)
    music_id = Column(Integer, ForeignKey('music.id'))
    music = relationship('Music', secondary=scene_music_association, back_populates='scenes')
