#!/usr/bin/node
// A script that prints the all characters of a Star War movie

const request = require('request-promise-native');

const fetchCharacters = async (movieID) => {
  // A function to fetch characters for a specific movieID

  try {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;
    const response = await request(url);
    const movie = JSON.parse(response);
    // console.log(movie)
    // console.log(`${movie.title}`);

    const sortedCharacters = await Promise.all(movie.characters.map(fetchCharacterDetails));
    sortedCharacters.sort((a, b) => {
      const getId = (url) => parseInt(url.split('/').slice(-2, -1)[0]);
      return getId(a.url) - getId(b.url);
    });

    sortedCharacters.forEach(character => {
      console.log(character.name);
    });
  } catch (e) {
    console.error(`Error fetching data: ${e}`);
  }
};

const fetchCharacterDetails = async (characterURL) => {
  // Function to fetch character details from a character URL
  try {
    const response = await request(characterURL);
    // console.log(JSON.parse(response));
    return JSON.parse(response);
  } catch (e) {
    console.error(`Error fetching character data: ${e}`);
  }
};

const movieID = process.argv[2];
if (movieID) {
  fetchCharacters(movieID);
}
