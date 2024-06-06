import { useAuthStore } from '@/stores/auth.store';

// Import các biến icon từ thư viện
import {
  mdiMenu,
  mdiClockOutline,
  mdiCloud,
  mdiCrop,
  mdiAccount,
  mdiCogOutline,
  mdiEmail,
  mdiLogout,
  mdiThemeLightDark,
  mdiGithub,
  mdiReact
} from '@mdi/js';

const userStore = useAuthStore();
const { isLoggedIn } = storeToRefs(userStore);
// Hàm để tạo menu khi người dùng đã đăng nhập
export const createLoggedInMenu = () => {
  const menu = [
    {
      label: 'Home',
    },
    {
      label: 'Plan Trip',
      href: '/chatbot',
    },
    {
      label: 'Resources',
      href: '/dashboard',
    },
    {
      label: 'Pricing',
      href: '/',
    },
    {
      label: 'Travel Blog',
      href: '/',
    },
    {
      isCurrentUser: true,
      menu: [
        {
          icon: mdiAccount,
          label: 'My Profile',
          to: '/profile'
        },
        {
          icon: mdiCogOutline,
          label: 'Settings'
        },
        {
          icon: mdiEmail,
          label: 'Messages'
        },
        {
          isDivider: true
        },
        {
          icon: mdiLogout,
          label: 'Log Out',
          isLogout: true
        }
      ]
    },
    {
      icon: mdiThemeLightDark,
      label: 'Light/Dark',
      isDesktopNoLabel: true,
      isToggleLightDark: true
    },
    {
      isButton: true,
    }
  ];

  return menu;
};

// Hàm để tạo menu khi người dùng chưa đăng nhập
export const createLoggedOutMenu = () => {
  const menu = [
    {
      label: 'Home',
    },
    {
      label: 'Plan Trip',
      href: '/chatbot',
    },
    {
      label: 'Resources',
      href: '/dashboard',
    },
    {
      label: 'Pricing',
      href: '/',
    },
    {
      label: 'Travel Blog',
      href: '/',
    },
    {
      icon: mdiThemeLightDark,
      label: 'Light/Dark',
      isDesktopNoLabel: true,
      isToggleLightDark: true
    },
    {
      isButton: true,
    }
  ];

  return menu;
};
// Tạo menu dựa trên trạng thái đăng nhập của người dùng
const menu = isLoggedIn ? createLoggedInMenu() : createLoggedOutMenu();

export default menu;