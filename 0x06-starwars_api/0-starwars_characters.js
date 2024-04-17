#!/usr/bin/node
// A script that prints the all characters of a Star War movie

const request = require('request');

const fetchCharacters = (movieID) => {
  // A function to fetch characters for a specific movieID

  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
    request(url, (error, response, body) => {
      if (error) {
        console.log(error);
        process.exit(1);
      }
      const movie = JSON.parse(body);
      // console.log(movie)
      // console.log(`${movie.title}`);

      const characterPromises = movie.characters.map(characterURL => fetchCharacterDetails(characterURL));

      Promise.all(characterPromises).then(characters => {
        characters.sort((a, b) => {
          const getId = (url) => parseInt(url.split('/').slice(-2, -1)[0]);
          return getId(a.url) - getId(b.url);
        });

        characters.forEach((character) => {
          console.log(character.name);
        });
      }).catch(e => console.error(`Error fetching character data ${e}`));
    });
  } catch (e) {
    console.error(`Error fetching data: ${e}`);
  }
};

const fetchCharacterDetails = (characterURL) => {
  // Function to fetch character details from a character URL
  return new Promise((resolve, reject) => {
    request(characterURL, (error, response, body) => {
      if (error) {
        reject(error);
      }
      // console.log(JSON.parse(body));
      const character = JSON.parse(body);
      resolve(character);
    });
  });
};

const movieID = process.argv[2];
if (movieID) {
  fetchCharacters(movieID);
}
