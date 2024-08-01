# Authorization token that must have been created previously. See : https://developer.spotify.com/documentation/web-api/concepts/authorization
const token = 'BQDrmO579WYNFezwN9zEygMjuXS46WuwEyvkvw8Inba7cOwCBXtLB8UHHkMvfpIO7fychSkYkuRZ5hJF4bvz1rOXguJuw6H_PqMeGXb2mQTJ5lu23BNoveFPoo_Ae9xGNTQXVJoFPoZcf5W1bvnRWg2vff1BXou91ysdjPwYm8S7I2yLggvirBW_RakRBbkWmOZIA4EGseWessy4EoSdiFrc4KfIHQfvxNMDI-4iVbnGT4VRQE7FH_aSCJGXoCUt3j4T3Xbl5XG0JRdbPw';
async function fetchWebApi(endpoint, method, body) {
  const res = await fetch(`https://api.spotify.com/${endpoint}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
    method,
    body:JSON.stringify(body)
  });
  return await res.json();
}

async function getTopTracks(){
#    Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
  return (await fetchWebApi(
    'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
  )).items;
}

const topTracks = await getTopTracks();
console.log(
  topTracks?.map(
    ({name, artists}) =>
      `${name} by ${artists.map(artist => artist.name).join(', ')}`
  )
);