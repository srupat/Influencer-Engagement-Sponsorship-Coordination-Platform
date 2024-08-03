// store/plugins/localStorage.js

export default store => {
    store.subscribe((mutation, state) => {
      localStorage.setItem('sponsorID', state.sponsorID);
    });
  };
  