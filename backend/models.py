
from sqlalchemy import Column, Integer, String, Float, JSON, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GenerationJob(Base):
    __tablename__ = "generation_jobs"
    
    id = Column(Integer, primary_key=True)
    job_id = Column(String, unique=True)
    status = Column(String)  # pending, processing, completed, failed
    music_file_hash = Column(String)
    analysis_data = Column(JSON)
    generated_video_url = Column(String)
    created_at = Column(DateTime)
    completed_at = Column(DateTime)
    credit_cost = Column(Float)