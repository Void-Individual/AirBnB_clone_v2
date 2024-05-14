#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from models import storage
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    """Define relationship for DBStorage"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place',
                                cascade='all, delete-orphan')
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False)

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True, default='None')
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)

    @property
    def reviews(self):
        """For FileStorage instead of DBStorage"""

        from models.review import Review
        objects = storage.all(Review)
        rev = []
        for key, value in objects.items():
            if key.split('.')[0] == 'Review':
                if value.__dict__['place_id'] == self.id:
                    rev.append(value)
        return rev

    @property
    def amenities(self):
        """To retrive using FileStorage"""

        from models.amenity import Amenity
        objects = storage.all(Amenity)
        amen = []
        for amenity_id in self.amenity_ids:
            for key, value in objects.items():
                if key.split('.')[0] == "Amenity":
                    amenity = value.__dict__['amenity_id']
                    if amenity == amenity_id:
                        amen.append(amenity)
        return amen

    @amenities.setter
    def amenities(self, amenity):
        """Setter attribut to append Amenity.id to amenity_ids"""

        from models.amenity import Amenity
        if isinstance(amenity, Amenity):
            if not hasattr(self, 'amenity_ids'):
                setattr(self, 'amenity_ids', [])
            self.amenity_ids.append(amenity.id)
