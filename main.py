import discord
import sqlite3
import os

class BoatsBot:

  insert_example = """
  INSERT INTO boats (user, to_boat_count, boats_count, mention) VALUES ('chris', 0, 0, '@chris')
  """

  def __init_db(self):
    cur = self.db.cursor()
    sql = """
    CREATE TABLE IF NOT EXISTS boats (
      user TEXT PRIMARY KEY,
      to_boat_count INTEGER NOT NULL,
      boats_count INTEGER NOT NULL,
      mention TEXT NOT NULL
    )
    """
    cur.executescript(sql)
    self.db.commit()
    cur.close()

  def get_to_boat(self, author) -> int:
    cur = self.db.cursor()
    sql = f"""
    SELECT * FROM boats WHERE user = '{author.name}'
    """
    cur.execute(sql)
    rows = cur.fetchall()
    if len(rows) < 1:
      # insert/init author
      cur.close
      return 4
    else:
      to_boat = rows[0][1]
      cur.close()
      return to_boat

  def update_boats(self, author, count: int = 1) -> None:
    if author.id in db.keys():
      db[author.id] += count
    else:
      db[author.id] = count

  def __init__(self, db: str = 'boatsbot.db') -> None:
    self.client = discord.Client()
    self.db = None
    try:
      self.db = sqlite3.connect(db)
    except Error as e:
      print(e)
    self.__init_db()


  def start(self, token: str = os.getenv('TOKEN')) -> None:
    client.run(token)

  @client.event
  async def on_ready(self) -> None:
    print('We have logged in as {0.user}'.format(client))

  @client.event
  async def on_message(self, message):
    bizz_count = 0
    buzz_count = 0

    if message.author == client.user:
      return

    if message.content.startswith('$leaderboard'):
      await message.channel.send('All-Time boat count:')

    elif message.content.startswith('$boats'):
      to_boat = get_to_boat(message.author)
      await message.channel.send(f'You are {to_boat} to boat')

    bizz_count = message.content.count('five') + message.content.count('5')
    buzz_count = message.content.count('seven') + message.content.count('7')
    boats_count = bizz_count + buzz_count
    to_boat = get_to_boat(message.author)

    if boats_count > 0:
      print(f"updating count with: {boats_count}")
      update_boats(message.author, count=boats_count)
      bizz_word = "bizzes" if bizz_count != 1 else "bizz"
      buzz_word = "buzzes" if buzz_count != 1 else "buzz"
      boats_string = "" if to_boat - boats_count > 0 else f"you're boats @{message.author}, "
      new_to_boat = (to_boat - boats_count) if (to_boat - boats_count) > 0 else 4-abs(to_boat - boats_count)
      await message.channel.send(f"you dropped {bizz_count} {bizz_word} and {buzz_count} {buzz_word}, {boats_string}{new_to_boat} to boat")

if __name__ == "__main__":
  bot = BoatsBot()
  bot.start()