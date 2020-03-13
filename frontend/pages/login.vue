<template>
  <div>
    <v-row>
      <v-col>
        <h2 class="text-center">
          Sign in to Arxiv Bookmark
        </h2>
      </v-col>
    </v-row>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-text class="pb-0">
            <v-form>
              <p class="mb-0">
                Email
              </p>
              <v-text-field v-model="form.username" outlined dense name="username" type="text" />
              <p class="mb-0">
                Password
              </p>
              <v-text-field
                id="password"
                v-model="form.password"
                outlined
                dense
                name="password"
                type="password"
              />
            </v-form>
          </v-card-text>
          <v-card-actions class="pl-4 pr-4">
            <v-btn class="mb-2" color="success" block @click="login">
              Sign in
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <v-row>
      <v-col>
        <p class="text-center">
          New to Arxiv Bookmark?
          <nuxt-link to="/register">
            Create an account.
          </nuxt-link>
        </p>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: 'Login',
  layout: 'auth',
  middleware ({ store, redirect }) {
    if (store.$auth.loggedIn) {
      redirect('/')
    }
  },
  data () {
    return {
      form: {
        username: '',
        password: ''
      }
    }
  },
  methods: {
    async login () {
      try {
        await this.$auth.loginWith('local', {
          data: `username=${this.form.username}&password=${this.form.password}`
        })
      } catch (error) {
        // eslint-disable-next-line no-console
        console.log(error)
      }
    }
  }
}
</script>

<style scoped>

</style>
