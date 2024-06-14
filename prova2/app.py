from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from log_config import LoggerSetup
import logging

app = FastAPI()

# Cria um logger raiz
logger_setup = LoggerSetup()

# Adiciona o logger para o módulo
logger = logging.getLogger(__name__)

logging.basicConfig(
    filename='informations_blog.log',
    level=logging.WARNING, 
    format='%(asctime)s:%(levelname)s:%(message)s'
)

blog_posts = []

class BlogPost(BaseModel):
    id: int
    title: str
    content: str

@app.post('/blog', status_code=201)
def create_blog_post(post: BlogPost):
    blog_posts.append(post)
    logging.info(f'New blog post created with id {post.id}')
    return {'status': 'success'}

@app.get('/blog', response_model=List[BlogPost])
def get_blog_posts():
    logging.info('Retrieving all blog posts')
    return blog_posts

@app.get('/blog/{id}', response_model=BlogPost)
def get_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            logging.info(f'Retrieving blog post with id {id}')
            return post
    logging.error(f'Blog post with id {id} not found')
    raise HTTPException(status_code=404, detail='Post not found')

@app.delete('/blog/{id}', status_code=200)
def delete_blog_post(id: int):
    for post in blog_posts:
        if post.id == id:
            blog_posts.remove(post)
            logging.warning(f'Blog post with id {id} deleted')
            return {'status': 'success'}
    logging.error(f'Blog post with id {id} not found')
    raise HTTPException(status_code=404, detail='Post not found')

@app.put('/blog/{id}', status_code=200)
def update_blog_post(id: int, updated_post: BlogPost):
    for post in blog_posts:
        if post.id == id:
            post.title = updated_post.title
            post.content = updated_post.content
            logging.info(f'Blog post with id {id} updated')
            return {'status': 'success'}
    logging.error(f'Blog post with id {id} not found')
    raise HTTPException(status_code=404, detail='Post not found')
