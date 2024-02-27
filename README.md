# Museum and Famous Paintings Data Analysis

## Overview

This project analyzes the Famous Paintings dataset obtained from Kaggle. The dataset contains information about various famous paintings, including details about the artist, subject, year and museums.

![image](https://github.com/Sameer1295/Museum-Data-Analysis-in-SQL/assets/29782669/0880cb26-77d6-4c49-a9a6-806291b6b3d6)

## Database Schema

### Entity-Relationship (ER) Diagram:

The ER diagram represents the structure of the database, detailing the entities and their relationships.

#### Entities:

1. **Artist:**
   - Attributes: artist_id, full_name, first_name, middle_names, last_name, nationality, style, birth, death
   - Primary Key: artist_id

2. **Canvas Size:**
   - Attributes: size_id, width, height, label
   - Primary Key: size_id

3. **Image Link:**
   - Attributes: work_id, url, thumbnail_small_url, thumbnail_large_url
   - Primary Key: work_id
   - Foreign Key: work_id references Work(work_id)

4. **Museum:**
   - Attributes: museum_id, name, address, city, state, postal, country, phone, url
   - Primary Key: museum_id

5. **Museum Hours:**
   - Attributes: museum_id, day, open, close
   - Primary Key: museum_id
   - Foreign Key: museum_id references Museum(museum_id)

6. **Product Size:**
   - Attributes: work_id, size_id, sale_price, regular_price
   - Primary Key: work_id
   - Foreign Key: work_id references Work(work_id)

7. **Subject:**
   - Attributes: work_id, subject
   - Primary Key: work_id
   - Foreign Key: work_id references Work(work_id)

8. **Work:**
   - Attributes: work_id, name, artist_id, style, museum_id
   - Primary Key: work_id
   - Foreign Keys: artist_id references Artist(artist_id), museum_id references Museum(museum_id)

#### Relationships:

- **Artist - Work:**
  - One-to-Many relationship: An artist can have multiple works, but each work is created by one artist.

- **Work - Museum:**
  - Many-to-One relationship: A work is associated with one museum, but a museum can have multiple works.

- **Museum - Museum Hours:**
  - One-to-Many relationship: A museum can have multiple opening hours, but each opening hour is associated with one museum.

- **Work - Image Link:**
  - One-to-One relationship: Each work has a unique image link.

- **Work - Product Size:**
  - One-to-One relationship: Each work has a unique product size.

- **Work - Subject:**
  - One-to-Many relationship: A work can have multiple subjects.

This ER diagram provides a visual representation of how the different entities in the database are related to each other, aiding in understanding the dataset structure and relationships.
