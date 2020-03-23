<template>
  <div>
    <v-card outlined>
      <v-card-title class="font-weight-bold pb-1">
        <nuxt-link :to="{name:'papers-id', params: {id:paper.id}}" target="_blank" class="link">
          {{ paper.title }}
        </nuxt-link>
      </v-card-title>
      <v-card-text class="pb-2">
        <!-- Authors -->
        <div>
          <span class="author font-weight-light">
            {{ reformatAuthors(paper.authors) }}
          </span>
        </div>
        <!-- calender -->
        <div>
          <span class="calender font-weight-light">
            {{ diffTimeFromNow(paper.updated) }}
          </span>
        </div>
        <!-- Summary -->
        <v-clamp :max-lines="clampMaxLines" class="body" autoresize>
          {{ paper.summary }}
        </v-clamp>
        <div class="mt-3 ml-3 mr-3">
          <v-row class="mt-1">
            <!-- New or update -->
            <span class="font-weight-bold mr-1 mb-1">
              <v-chip v-if="paper.is_new" label color="teal lighten-1" text-color="white" small>
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
              >
                {{ conference.name }}
              </v-chip>
            </span>
            <!-- Categories -->
            <v-chip
              small
              label
              class="mr-1 mb-1"
              color="grey lighten-2"
              text-color="grey darken-2"
            >
              {{ paper.arxiv_primary_category }}
            </v-chip>
            <v-spacer />
          </v-row>
        </div>
      </v-card-text>
      <v-divider class="mx-4" />
      <v-card-actions class="py-2">
        <v-row justify="space-around">
          <v-btn text small style="color: dimgrey" @click="bookmark(paper.id)">
            <v-icon v-if="isBookmarked()" style="color: crimson">
              mdi-bookmark-check
            </v-icon>
            <v-icon v-else>
              mdi-bookmark-outline
            </v-icon>
            Bookmark
          </v-btn>
          <v-btn text small style="color: dimgrey">
            <v-icon>
              mdi-comment-outline
            </v-icon>
            Comment
          </v-btn>
          <v-btn text small style="color: dimgrey">
            <v-icon>
              mdi-share-outline
            </v-icon>
            Share
          </v-btn>
        </v-row>
      </v-card-actions>
    </v-card>
    <v-alert
      v-model="alert"
      dense
      outlined
      type="warning"
      dismissible
      class="mt-2"
    >
      You must be signed in.
    </v-alert>
  </div>
</template>

<script>
import VClamp from 'vue-clamp'
export default {
  name: 'PaperCard',
  components: {
    VClamp
  },
  props: {
    paperProps: {
      type: Object,
      default () {
        return {
          id: 0,
          title: '',
          authors: [],
          summary: '',
          conferences: [],
          tags: [],
          arxiv_primary_category: '',
          published: '',
          updated: '',
          is_new: false,
          bookmark_users: {}
        }
      }
    }
  },
  data () {
    return {
      paper: this.paperProps,
      clampMaxLines: 6,
      alert: false,
      bookmarkIn: { paper_id: null, user_id: null }
    }
  },
  methods: {
    reformatAuthors (authors) {
      const authorsList = []
      for (let i = 0; i < authors.length; i++) {
        authorsList.push(authors[i].name)
      }
      return authorsList.join(', ')
    },
    diffTimeFromNow (date) {
      const now = new Date()
      const src = new Date(date)
      const diffTime = now.getTime() - src.getTime()
      const diffHour = Math.floor(diffTime / (1000 * 60 * 60))
      const diffDate = Math.floor(diffTime / (1000 * 60 * 60 * 24))
      const diffMonth = Math.floor(diffTime / (1000 * 60 * 60 * 24 * 30))
      const diffYear = Math.floor(diffTime / (1000 * 60 * 60 * 365))
      if (diffYear) {
        if (diffYear === 1) {
          return '1 YEAR AGO'
        } else {
          return `${diffYear} YEARS AGO`
        }
      } else if (diffMonth) {
        if (diffMonth === 1) {
          return '1 MONTH AGO'
        } else {
          return `${diffMonth} MONTHS AGO`
        }
      } else if (diffDate) {
        if (diffDate === 1) {
          return '1 DAY AGO'
        } else {
          return `${diffDate} DAYS AGO`
        }
      } else if (diffHour > 1) {
        return `${diffHour} HOURS AGO`
      } else {
        return '1 HOURS AGO'
      }
    },
    // Parse datetime
    parseDate (date) {
      const d = new Date(date)
      return `${d.getUTCMonth() + 1}/${d.getUTCDate()}/${d.getUTCFullYear()}`
    },
    makeCalender (paper) {
      if (!paper.is_new) {
        return this.parseDate(paper.updated) + ` (v1: ${this.parseDate(paper.published)})`
      } else {
        return this.parseDate(paper.updated)
      }
    },
    async bookmark (paperId) {
      if (this.$auth.loggedIn) {
        this.bookmarkIn.paper_id = paperId
        this.bookmarkIn.user_id = this.$auth.user.id
        if (this.isBookmarked()) {
          this.paper = await this.$axios.$delete('/api/v1/bookmarks', { data: this.bookmarkIn })
        } else {
          this.paper = await this.$axios.$post('/api/v1/bookmarks', this.bookmarkIn)
        }
      } else {
        this.alert = true
      }
    },
    isBookmarked () {
      for (let i = 0; i < this.paper.bookmarks.length; i++) {
        if (this.paper.bookmarks[i].user_id === this.$auth.user.id) {
          return true
        }
      }
    }
  }
}
</script>

<style scoped>
  .author {
    font-size: small;
  }
  .calender {
    font-size: xx-small;
  }
  .link {
    color: black;
    background-color: transparent;
    text-decoration: none;
  }
  a:hover {
    color: dimgrey;
  }
</style>
