Решение тестового задания задания №1 нахоидится в файле sequence.py  

Проект магазина продуктов со следующим функционалом:  
Должна быть реализована возможность создания, редактирования, удаления категорий и подкатегорий товаров в админке.  
Категории и подкатегории обязательно должны иметь наименование, slug-имя, изображение  
Подкатегории должны быть связаны с родительской категорией  
Должен быть реализован эндпоинт для просмотра всех категорий с подкатегориями. Должны быть предусмотрена пагинация.  
Должна быть реализована возможность добавления, изменения, удаления продуктов в админке.  
Продукты должны относится к определенной подкатегории и, соответственно категории, должны иметь наименование, slug-имя, изображение в 3-х размерах, цену  
Должен быть реализован эндпоинт вывода продуктов с пагинацией. Каждый продукт в выводе должен иметь поля: наименование, slug, категория, подкатегория, цена, список изображений  
Реализовать эндпоинт добавления, изменения (изменение количества), удаления продукта в корзине.  
Реализовать эндпоинт вывода  состава корзины с подсчетом количества товаров и суммы стоимости товаров в корзине.  
Реализовать возможность полной очистки корзины  
Операции по эндпоинтам категорий и продуктов может осуществлять любой пользователь  
Операции по эндпоинтам корзины может осуществлять только авторизированный пользователь и только со своей корзиной  
Реализовать авторизацию по токену  
