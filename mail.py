U
    (��^�  �                   @   ��   d dl Z d dlZd dlZd dlZdZdZdZdZdZdd� Z	dd
d�Z
e
dd� ede� de� d��Zee� de� d��Zede� de� d��Zee� de� d��Zee� de� d��Ze	eeeee� dS )�    N�[1;32m�[1;37m�[1;35m�[1;36m�[1;31m�           
      C   �   t �d}t �td��� �� �}d|i}| ||||dd�}z8tj|||d�}	|	jdkrjtdt	� d	�� t
�d
� W n( tjjk
r�   tdt� d�� Y nX d S �N�8http://rajajatuhcinta.000webhostapp.com/email-script.php�ua.txt�
user-agent� �ZfromNameZ	fromEmailZtoEmail�subject�messageZsendMailBtn��headers�data��   �
�Email Succesfully Sent�   �Email Failed To Send��random�choice�open�read�
splitlines�requests�post�status_code�print�g�time�sleep�
exceptions�ConnectionError�r�
�name�prom�to�sbj�msg�url�uar   r   �run� r3   �x.py�send   �"    �
r5   F�                 C   �N   t �d� tdt� dt� dt� dt� dt� dt� d�� | d	k	rHtd
� d S �X�N�clearr   �____ ____ _  _ ____  �  ____ _  _ ____ _ _    
�|___ |__| |_/  |___  �  |___ |\/| |__| | |    
�|    |  | | \_ |___  �  |___ |  | |  | | |___ F�=[101m[37;1m::        Fake Email By Anonk Yuhuu       ::[0m��os�systemr#   �p�b��name_authorr3   r3   r4   �banner%   �     
������
rI   T�rH   r   �Name Sender �: �From Email � : �
 To Email �	 Subject �	 Message �F)r    rC   r   r%   r$   �wrE   rF   r)   r5   rI   �input�fromname�fromail�tomailr   �msgsr3   r3   r3   r4   �<module>   �    

