const localStoragePlugin = store => {
  store.subscribe((mutation, state) => {
    localStorage.setItem('sponsorID', state.sponsorID);
    localStorage.setItem('campaignID', state.campaignID);
  });
};

export default localStoragePlugin;
