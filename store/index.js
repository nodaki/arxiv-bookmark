export const state = () => ({
  papers: [],
  page: 0,
  categories: [],
  resetInfiniteLoading: false
})

export const getters = {
  getResetInfiniteLoadingFlag (state) {
    return state.resetInfiniteLoading
  }
}

export const mutations = {
  setCategories (state, categories) {
    state.categories = []
    state.categories.push(...categories)
  },
  addCategory (state, category) {
    state.categories.push(category)
  },
  addPapers (state, papers) {
    state.papers.push(...papers)
  },
  incrementPage (state) {
    state.page += 1
  },
  resetPapers (state) {
    state.papers = []
  },
  resetPage (state) {
    state.page = 0
  },
  setInfiniteLoadingFlag (state, flag) {
    state.resetInfiniteLoading = flag
  }
}
