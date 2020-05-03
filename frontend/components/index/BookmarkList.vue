<template>
  <div>
    <v-card max-height="500" outlined style="overflow-y: scroll">
      <v-card-subtitle>
        Bookmark
      </v-card-subtitle>
      <div v-for="(paper, i) in papersProps" :key="i">
        <v-card-title>
          <nuxt-link :to="{name:'papers-id', params: {id:paper.id}}" target="_blank" class="link body-1 font-weight-medium">
            {{ paper.title }}
          </nuxt-link>
        </v-card-title>
        <v-divider />
      </div>
    </v-card>
  </div>
</template>

<script>
export default {
  name: 'BookmarkList',
  props: {
    papersProps: {
      type: Array,
      default () {
        return {}
      }
    }
  }
}
</script>

<style scoped>
  .link {
    color: black;
    background-color: transparent;
    text-decoration: none;
  }
</style>
