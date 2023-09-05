# Создать базу данных Human_friends
create_db_query = """
    CREATE DATABASE Human_friends
    """

# Выбрать базу данных Human_friends
use_db_query = """
    USE Human_friends
    """

# Создать таблицу animals
create_table_animals = """
    CREATE TABLE animals
    (animals_id INT NOT NULL auto_increment PRIMARY KEY,
    animal_species VARCHAR(100));
    """

# Создать таблицу domestic_animals
create_table_domestic_animals = """
    CREATE TABLE domestic_animals
    (domestic_animals_id INT NOT NULL auto_increment PRIMARY KEY,
    animalsId INT,
    type_animal VARCHAR(100),
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу pack_animals
create_table_pack_animals = """
    CREATE TABLE pack_animals
    (pack_animals_id INT NOT NULL auto_increment PRIMARY KEY,
    animalsId INT,
    type_animal VARCHAR(100),
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу dogs
create_table_dogs = """
    CREATE TABLE dogs
    (dogs_id INT NOT NULL auto_increment PRIMARY KEY,
    domestic_animalsId INT,
    animalsId INT,
    dog_name VARCHAR(100),
    dog_birthday DATE,
    command_name VARCHAR(100),
    FOREIGN KEY (domestic_animalsId) REFERENCES domestic_animals (domestic_animals_id) ON DELETE CASCADE,
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу cats
create_table_cats = """
    CREATE TABLE cats
    (cats_id INT NOT NULL auto_increment PRIMARY KEY,
    domestic_animalsId INT,
    animalsId INT,
    cat_name VARCHAR(100),
    cat_birthday DATE,
    command_name VARCHAR(100),
    FOREIGN KEY (domestic_animalsId) REFERENCES domestic_animals (domestic_animals_id) ON DELETE CASCADE,
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу hamsters
create_table_hamsters = """
    CREATE TABLE hamsters
    (hamsters_id INT NOT NULL auto_increment PRIMARY KEY,
    domestic_animalsId INT,
    animalsId INT,
    hamster_name VARCHAR(100),
    hamster_birthday DATE,
    command_name VARCHAR(100),
    FOREIGN KEY (domestic_animalsId) REFERENCES domestic_animals (domestic_animals_id) ON DELETE CASCADE,
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу horses
create_table_horses = """
    CREATE TABLE horses
    (horses_id INT NOT NULL auto_increment PRIMARY KEY,
    pack_animalsId INT,
    animalsId INT,
    horse_name VARCHAR(100),
    horse_birthday DATE,
    command_name VARCHAR(100),
    FOREIGN KEY (pack_animalsId) REFERENCES pack_animals (pack_animals_id) ON DELETE CASCADE,
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу camels
create_table_camels = """
    CREATE TABLE camels
    (camels_id INT NOT NULL auto_increment PRIMARY KEY,
    pack_animalsId INT,
    animalsId INT,
    camel_name VARCHAR(100),
    camel_birthday DATE,
    command_name VARCHAR(100),
    FOREIGN KEY (pack_animalsId) REFERENCES pack_animals (pack_animals_id) ON DELETE CASCADE,
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Создать таблицу donkeys
create_table_donkeys = """
    CREATE TABLE donkeys
    (donkeys_id INT NOT NULL auto_increment PRIMARY KEY,
    pack_animalsId INT,
    animalsId INT,
    donkey_name VARCHAR(100),
    donkey_birthday DATE,
    command_name VARCHAR(100),
    FOREIGN KEY (pack_animalsId) REFERENCES pack_animals (pack_animals_id) ON DELETE CASCADE,
    FOREIGN KEY (animalsId) REFERENCES animals (animals_id) ON DELETE CASCADE);
    """

# Вставка записей в таблицу animals
insert_animals_query = """
    INSERT INTO animals (animal_species) 
    VALUES 
        ("Domestic animals"), 
        ("Pack animals")
    """

# Вставка записей в таблицу domestic_animals
insert_domestic_animals_query = """
    INSERT INTO domestic_animals (animalsId, type_animal) 
    VALUES 
        (1, "dogs"), 
        (1, "cats"),
        (1, "hamsters")
    """

# Вставка записей в таблицу pack_animals
insert_pack_animals_query = """
    INSERT INTO pack_animals (animalsId, type_animal) 
    VALUES 
        (2, "horses"), 
        (2, "camels"),
        (2, "donkeys")
    """

# Вставка записей в таблицу dogs
insert_dogs_query = """
    INSERT INTO dogs (domestic_animalsId, animalsId, dog_name, dog_birthday, command_name) 
    VALUES 
        (1, 1, "Шарик", "2018-06-12", "come here")
    """

# Вставка записей в таблицу cats
insert_cats_query = """
    INSERT INTO cats (domestic_animalsId, animalsId, cat_name, cat_birthday, command_name) 
    VALUES 
        (2, 1, "Мурзик", "2023-05-19", "come here")
    """

# Вставка записей в таблицу hamsters
insert_hamsters_query = """
    INSERT INTO hamsters (domestic_animalsId, animalsId, hamster_name, hamster_birthday, command_name) 
    VALUES 
        (3, 1, "Прошка", "2016-07-10", "run")
    """

# Вставка записей в таблицу horses
insert_horses_query = """
    INSERT INTO horses (pack_animalsId, animalsId, horse_name, horse_birthday, command_name) 
    VALUES 
        (1, 2, "Шустрый", "2018-03-12", "jump")
    """

# Вставка записей в таблицу camels
insert_camels_query = """
    INSERT INTO camels (pack_animalsId, animalsId, camel_name, camel_birthday, command_name) 
    VALUES 
        (2, 2, "Высокий", "2023-02-19", "transport")
    """

# Вставка записей в таблицу donkeys
insert_donkeys_query = """
    INSERT INTO donkeys (pack_animalsId, animalsId, donkey_name, donkey_birthday, command_name) 
    VALUES 
        (3, 2, "Упертый", "2016-07-02", "transport")
    """

# Удалить из таблицы верблюдов
delete_query = """
    DELETE FROM camels WHERE pack_animalsId = 2;
    """

# Выбрать таблицы лошади и ослы в одной таблице
union_horses_donkeys_query = """
    SELECT * FROM horses UNION SELECT * FROM donkeys;
    """

# Объединить таблицы лошадей и ослов в одну таблицу
create_table_horses_and_donkeys_query = """
    CREATE TABLE horses_and_donkeys 
    (horses_and_donkeys_id INT NOT NULL auto_increment PRIMARY KEY)
    SELECT * FROM horses UNION SELECT * FROM donkeys;
    """

# Создать новую таблицу young_animals, в которую попадут все
# животные старше 1 года, но младше 3 лет, и в отдельном столбце с точностью
# до месяца подсчитать возраст животных в новой таблице
create_table_young_animals_query = """
    CREATE TABLE young_animals (young_animals_id INT NOT NULL auto_increment PRIMARY KEY)
    SELECT 
        dog_name, 
        dog_birthday, 
        command_name,
        Round((year(current_date()) - year(dog_birthday)) + (month(current_date() - month(dog_birthday)))/10, 2) as age
    FROM dogs
    WHERE Round((year(current_date()) - year(dog_birthday)) + (month(current_date() - month(dog_birthday)))/10, 2) > 1 
	and Round((year(current_date()) - year(dog_birthday)) + (month(current_date() - month(dog_birthday)))/10, 2) < 3
	UNION SELECT
	    cat_name, 
        cat_birthday, 
        command_name,
        Round((year(current_date()) - year(cat_birthday)) + (month(current_date() - month(cat_birthday)))/10, 2) as age
    FROM cats
    WHERE Round((year(current_date()) - year(cat_birthday)) + (month(current_date() - month(cat_birthday)))/10, 2) > 1 
	and Round((year(current_date()) - year(cat_birthday)) + (month(current_date() - month(cat_birthday)))/10, 2) < 3
    UNION SELECT
	    hamster_name, 
        hamster_birthday, 
        command_name,
        Round((year(current_date()) - year(hamster_birthday)) + (month(current_date() - month(hamster_birthday)))/10, 2) as age
    FROM hamsters
    WHERE Round((year(current_date()) - year(hamster_birthday)) + (month(current_date() - month(hamster_birthday)))/10, 2) > 1 
	and Round((year(current_date()) - year(hamster_birthday)) + (month(current_date() - month(hamster_birthday)))/10, 2) < 3
    UNION SELECT
	    horse_name, 
        horse_birthday, 
        command_name,
        Round((year(current_date()) - year(horse_birthday)) + (month(current_date() - month(horse_birthday)))/10, 2) as age
    FROM horses
    WHERE Round((year(current_date()) - year(horse_birthday)) + (month(current_date() - month(horse_birthday)))/10, 2) > 1 
	and Round((year(current_date()) - year(horse_birthday)) + (month(current_date() - month(horse_birthday)))/10, 2) < 3
	UNION SELECT
	    camel_name, 
        camel_birthday, 
        command_name,
        Round((year(current_date()) - year(camel_birthday)) + (month(current_date() - month(camel_birthday)))/10, 2) as age
    FROM camels
    WHERE Round((year(current_date()) - year(camel_birthday)) + (month(current_date() - month(camel_birthday)))/10, 2) > 1 
	and Round((year(current_date()) - year(camel_birthday)) + (month(current_date() - month(camel_birthday)))/10, 2) < 3
	UNION SELECT
	    donkey_name, 
        donkey_birthday, 
        command_name,
        Round((year(current_date()) - year(donkey_birthday)) + (month(current_date() - month(donkey_birthday)))/10, 2) as age
    FROM donkeys
    WHERE Round((year(current_date()) - year(donkey_birthday)) + (month(current_date() - month(donkey_birthday)))/10, 2) > 1 
	and Round((year(current_date()) - year(donkey_birthday)) + (month(current_date() - month(donkey_birthday)))/10, 2) < 3;
    """

# Объединить все таблицы в одну, при этом сохраняя поля, указывающие на
# прошлую принадлежность к старым таблицам
create_table_all_animals_query = """
    CREATE TABLE joint_table_human_friend (joint_table_id INT NOT NULL auto_increment PRIMARY KEY)
    SELECT  
        dog_name, 
        dog_birthday,
        command_name,
        'dogs' as old_table
    FROM dogs 
    UNION SELECT
        cat_name, 
        cat_birthday,
        command_name,
        'cats' as old_table
    FROM cats
    UNION SELECT
        hamster_name, 
        hamster_birthday,
        command_name,
        'hamsters' as old_table
    FROM hamsters
    UNION SELECT
        horse_name, 
        horse_birthday,
        command_name,
        'horses' as old_table
    FROM horses
    UNION SELECT
        camel_name, 
        camel_birthday,
        command_name,
        'camels' as old_table
    FROM camels
    UNION SELECT
        donkey_name, 
        donkey_birthday,
        command_name,
        'donkeys' as old_table
    FROM donkeys;
    """
