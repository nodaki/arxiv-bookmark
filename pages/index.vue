<template>
  <div>
    <v-row v-for="(paper, i) in papers" :key="i">
      <v-col>
        <v-card>
          <v-card-title class="mb-2" @click="openDialog(paper)">
            {{ paper.title }}
          </v-card-title>
          <v-card-text>
            <!-- Authors -->
            <div>
              <v-chip class="caption mr-1 mb-2" outlined x-small label color="brown lighten-1">
                <v-icon left small>
                  mdi-account-circle-outline
                </v-icon>
                {{ paper.authors[0].name[0] }}
              </v-chip>
              <v-chip
                v-for="(author, j) in paper.authors.slice(1)"
                :key="j"
                class="caption mr-1 mb-2 hidden-xs-only"
                outlined
                x-small
                label
                color="brown lighten-1"
              >
                <v-icon left small>
                  mdi-account-circle-outline
                </v-icon>
                {{ author.name[0] }}
              </v-chip>
            </div>
            <!-- Summary -->
            <v-clamp class="body mt-2" autoresize :max-lines="clampMaxLines">
              {{ paper.summary }}
            </v-clamp>
            <div class="mt-4 ml-3 mr-3">
              <v-row class="mt-1">
                <!-- New or update -->
                <span class="font-weight-bold mr-1 mb-1">
                  <v-chip v-if="paper.isNew" label color="teal lighten-1" text-color="white" small>
                    New
                  </v-chip>
                  <v-chip v-else label color="teal lighten-3" text-color="white" small>
                    Updated
                  </v-chip>
                </span>
                <!-- Conference -->
                <span class="font-weight-bold">
                  <v-chip
                    v-for="(conference, j) in paper.conferences"
                    :key="j"
                    label
                    color="amber lighten-1"
                    text-color="white"
                    small
                    class="mr-1 mb-1"
                    @click="setComment(conference)"
                  >
                    {{ conference }}
                  </v-chip>
                </span>
                <!-- Categories -->
                <v-chip
                  v-for="(category, k) in paper.categories"
                  :key="k"
                  small
                  label
                  class="mr-1 mb-1"
                  color="grey lighten-2"
                  text-color="grey darken-2"
                >
                  {{ category.$.term }}
                </v-chip>
                <v-spacer />
                <!-- Calendar -->
                <div class="hidden-xs-only">
                  <v-icon x-small>
                    calendar_today
                  </v-icon>
                  <span class="caption">
                    {{ paper.updated.year }}/{{ paper.updated.month }}/{{ paper.updated.day }}
                  </span>
                  <span v-if="!paper.isNew" class="caption">
                    (v1: {{ paper.published.year }}/{{ paper.published.month }}/{{ paper.published.day }})
                  </span>
                </div>
              </v-row>
              <v-row>
                <!-- Calendar -->
                <div class="d-flex d-sm-none mt-1">
                  <v-icon x-small>
                    calendar_today
                  </v-icon>
                  <span class="caption">
                    {{ paper.updated.year }}/{{ paper.updated.month }}/{{ paper.updated.day }}
                  </span>
                  <span v-if="!paper.isNew" class="caption">
                    (v1: {{ paper.published.year }}/{{ paper.published.month }}/{{ paper.published.day }})
                  </span>
                </div>
              </v-row>
            </div>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
    <!-- Dialog -->
    <v-row>
      <v-col>
        <v-dialog v-model="dialog" max-width="800" scrollable>
          <v-card>
            <v-card-text id="scroll-target">
              <!-- Title -->
              <div class="title text--primary pb-3 pt-5">
                {{ dialogContent.title }}
              </div>
              <!-- Authors -->
              <div class="pb-1">
                <v-chip
                  v-for="(author, j) in dialogContent.authors"
                  :key="j"
                  class="caption mr-1 mb-2"
                  outlined
                  x-small
                  label
                  color="brown lighten-1"
                >
                  <v-icon left x-small>
                    mdi-account-circle-outline
                  </v-icon>
                  {{ author.name[0] }}
                </v-chip>
              </div>
              <div class="pb-2">
                <!-- Calendar -->
                <v-icon x-small>
                  calendar_today
                </v-icon>
                <span class="caption">
                  {{ dialogContent.updated.year }}/{{ dialogContent.updated.month }}/{{ dialogContent.updated.day }}
                </span>
                <span v-if="!dialogContent.isNew" class="caption">
                  (v1: {{ dialogContent.published.year }}/{{ dialogContent.published.month }}/{{ dialogContent.published.day }})
                </span>
              </div>
              <!-- Abstract -->
              <div class="text-center text--primary pb-1">
                Abstract
              </div>
              <!-- Abstract -->
              <div class="text--primary">
                {{ dialogContent.summary }}
              </div>
              <!-- Comment -->
              <div class="caption pt-2">
                Comment: {{ dialogContent.comment }}
              </div>
            </v-card-text>
            <v-divider />
            <!-- Actions -->
            <v-card-actions>
              <div class="flex-grow-1" />
              <v-btn color="primary" text @click="dialog = false">
                Close
              </v-btn>
              <v-btn color="primary" :href="dialogContent.pdf" target="_blank">
                Full Text
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>
    </v-row>
    <!-- Infinite Loading -->
    <div>
      <infinite-loading ref="infiniteLoading" spinner="spiral" @infinite="infiniteHandler" />
    </div>
  </div>
</template>

<script>
import { mapState, mapMutations, mapGetters } from 'vuex'
import VClamp from 'vue-clamp'
export default {
  components: {
    VClamp
  },
  data () {
    return {
      clampMaxLines: 3,
      maxResults: 10,
      initCat: ['cs.CV'],
      comment: '',
      baseUrl: 'https://export.arxiv.org/api/query?sortBy=lastUpdatedDate&sortOrder=descending&search_query=',
      dialog: false,
      dialogContent: { title: '', summary: '', pdf: '', authors: [], comment: '', published: '', updated: '', isNew: null }
    }
  },
  computed: {
    ...mapState({
      papers: state => state.papers,
      page: state => state.page,
      categories: state => state.categories
    }),
    ...mapGetters([
      'getResetInfiniteLoadingFlag'
    ])
  },
  watch: {
    getResetInfiniteLoadingFlag (val) {
      if (val) {
        this.resetInfiniteLoading()
        this.setInfiniteLoadingFlag(false)
      }
    }
  },
  mounted () {
    this.setCategories(this.initCat)
  },
  methods: {
    ...mapMutations([
      'setCategories',
      'addCategory',
      'addPapers',
      'incrementPage',
      'resetPapers',
      'resetPage',
      'setInfiniteLoadingFlag'
    ]),
    async asyncGetPapers (url) {
      const Parser = require('rss-parser')
      const options = {
        customFields: {
          item: [
            ['published', 'published'],
            ['updated', 'updated'],
            ['summary', 'summary'],
            ['author', 'authors', { keepArray: true }],
            ['category', 'categories', { keepArray: true }],
            ['arxiv:comment', 'comment']
          ]
        }
      }
      const parser = new Parser(options)
      const papers = []
      const parseDate = (date) => {
        return {
          year: date.getUTCFullYear(),
          month: date.getUTCMonth() + 1,
          day: date.getUTCDate()
        }
      }
      const feed = await parser.parseURL(url)
      feed.items.forEach(function (entry) {
        const pubDate = new Date(entry.published)
        const updatedDate = new Date(entry.updated)
        // Check whether new or update
        const isNew = entry.published === entry.updated
        let comment
        if (entry.comment) {
          comment = entry.comment._
        } else {
          comment = ''
        }
        // Get conference info from comment.
        const searchConferences = ['CVPR', 'ICCV', 'ACCV', 'ECCV', 'NIPS', 'NeurIPS', 'SIGGRAPH', 'AAAI', 'ICML', 'IJCAI']
        const conferences = []
        searchConferences.forEach(function (conference) {
          if (comment.includes(conference)) {
            conferences.push(conference)
          }
        })
        papers.push({
          title: entry.title,
          link: entry.link,
          pdf: `https://arxiv.org/pdf/${entry.link.split('/')[4]}.pdf`,
          id: entry.id,
          published: parseDate(pubDate),
          updated: parseDate(updatedDate),
          summary: entry.summary,
          authors: entry.authors,
          categories: entry.categories,
          comment,
          conferences,
          isNew
        })
      })
      return papers
    },
    async infiniteHandler ($state) {
      // Infinite loading
      if (this.loading) { return }
      try {
        this.loading = false
        const start = `&start=${this.page * this.maxResults}`
        const andOperator = '+AND+'
        // Categories
        const cat = []
        this.categories.forEach(function (category) {
          cat.push(`cat:${category}`)
        })
        const searchCat = cat.join('+OR+')
        let searchQuery
        if (this.comment) {
          searchQuery = searchCat + andOperator + `co:${this.comment}`
        } else {
          searchQuery = searchCat
        }
        const url = this.baseUrl + searchQuery + start + `&max_results=${this.maxResults}`
        const papers = await this.asyncGetPapers(url)
        this.addPapers(papers)
        this.incrementPage()
        $state.loaded()
      } catch (e) {
        $state.complete()
      } finally {
        this.loading = false
      }
    },
    resetInfiniteLoading () {
      this.resetPapers()
      this.resetPage()
      // Reset infinite loading
      this.$refs.infiniteLoading.stateChanger.reset()
    },
    setComment (comment) {
      this.comment = comment
      this.resetInfiniteLoading()
    },
    openDialog (paper) {
      this.dialogContent.title = paper.title
      this.dialogContent.summary = paper.summary
      this.dialogContent.pdf = paper.pdf
      this.dialogContent.authors = paper.authors
      this.dialogContent.comment = paper.comment
      this.dialogContent.published = paper.published
      this.dialogContent.updated = paper.updated
      this.dialogContent.isNew = paper.isNew
      this.dialog = true
      // Set scroll top to 0
      this.$nextTick(() => {
        const i = document.getElementById('scroll-target')
        i.attributes[1].ownerElement.scrollTop = 0
      })
    }
  }
}
</script>
